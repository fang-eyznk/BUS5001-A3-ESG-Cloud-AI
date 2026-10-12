"""Conceptual Dialogflow CX webhook for GreenDesk (NOT deployed - design illustration for Q1).

Deployed as a Cloud Run function, it would be called from the "Confirm Report" -> "Report Submitted"
transition with tag "create-incident". It creates a ticket in the facilities system and publishes a
de-identified event for ESG analytics (Pub/Sub -> BigQuery -> Looker Studio).
"""
import json, os, uuid, datetime
import functions_framework                    # Cloud Run functions runtime
from google.cloud import pubsub_v1           # analytics event bus

TOPIC = os.environ.get("ESG_TOPIC", "projects/corvale-esg/topics/esg-incidents")
publisher = pubsub_v1.PublisherClient()


def create_ticket(payload):
    """Placeholder for the ServiceNow / Jira Service Management REST call.
    Credentials come from Secret Manager, never from code or the agent export."""
    return "GD-" + datetime.date.today().strftime("%y%m%d") + "-" + uuid.uuid4().hex[:4].upper()


@functions_framework.http
def webhook(request):
    body = request.get_json(silent=True) or {}
    tag = body.get("fulfillmentInfo", {}).get("tag")
    p = body.get("sessionInfo", {}).get("parameters", {})
    if tag != "create-incident":
        return {"fulfillment_response": {"messages": []}}

    ticket = create_ticket(p)
    # De-identified analytics event: no email, no free-text location (data minimisation)
    event = {"ticket": ticket, "incident_type": p.get("incident_type"), "building": p.get("building"),
             "urgency": p.get("urgency"), "priority": p.get("priority"), "team": p.get("assigned_team"),
             "anonymous": p.get("contact_preference", "").startswith("anonymous"),
             "reported_at": datetime.datetime.utcnow().isoformat() + "Z"}
    publisher.publish(TOPIC, json.dumps(event).encode("utf-8"))

    return {
        "sessionInfo": {"parameters": {"ticket_id": ticket}},
        "fulfillment_response": {"messages": [{"text": {"text": [f"Your reference number is {ticket}."]}}]},
    }
