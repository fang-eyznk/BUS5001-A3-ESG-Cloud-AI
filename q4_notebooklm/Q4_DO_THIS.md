# Q4: exactly what to do (about 60 minutes)

You only do 3 things: (1) run each step in NotebookLM, (2) take ONE screenshot per step,
(3) copy-paste the answer text under that step in this file. Claude does the scoring and writes the analysis.

Screenshots: save them in the `screenshots/` folder with the names shown (e.g. `F1.png`).
Mac: Cmd+Shift+4, drag around the answer, then rename the file.

---------------------------------------------------------------------------------------------------
## STEP 0: Set up (10 min)

1. Go to https://notebooklm.google.com (it may now be called "Gemini Notebook"; same thing). Sign in.
2. Click **Create new notebook**. Name it: `BUS5001 A3 - AU climate disclosure briefing`
3. Add these sources (**+ Add source**):
   - **Website**: https://asic.gov.au/regulatory-resources/sustainability-reporting/
   - **Website**: https://www.ifrs.org/issued-standards/ifrs-sustainability-standards-navigator/ifrs-s2-climate-related-disclosures/
   - **PDF**: AASB S2 Climate-related Disclosures (Google "AASB S2 pdf", download from aasb.gov.au, upload)
   - **PDF**: ASIC Regulatory Guide 280 Sustainability reporting (Google "ASIC RG 280 pdf", download, upload)
   - **PDF**: latest sustainability/climate report of TWO big Australian companies
     (e.g. Woolworths Group and Telstra; Google "<company> climate report 2025 pdf")
   If a PDF is too big to upload, skip it and write which one below.
4. Screenshot the notebook showing the source list -> `F0_sources.png`

Sources added (write the names):
>

Date/time of test:
>

---------------------------------------------------------------------------------------------------
## STEP 1: Chat with citations (10 min)  -> screenshot `F1.png`

Type each question in the chat box. After the answer, click 2-3 of the small citation numbers and
look whether the highlighted source text really says the same thing.

Q1: `Which entities must prepare a sustainability report under the Australian regime, and from when? Give the three groups with their thresholds.`
Answer (paste):
>
Under Chapter 2M of the *Corporations Act 2001*, entities must prepare an annual sustainability report if they are required to prepare an annual financial report under Chapter 2M and meet one of the legislative reporting thresholds. 

### **Obligated Entities**
The reporting requirement applies to:
* **Companies** (including registered corporations under the *National Greenhouse and Energy Reporting Act 2007* / NGER Act).
* **Registered managed investment schemes**.
* **Registrable Superannuation Entities (RSEs)**.
* **Retail Corporate Collective Investment Vehicles (CCIVs)**.

*(Note: Foreign registered companies, small proprietary companies without Chapter 2M obligations, and registered charities reporting solely under the ACNC Act are generally exempt).*

---

### **The Three Reporting Cohorts & Thresholds**

The regime is phased in across three groups based on corporate size, emissions reporting status, or asset values:

#### **1. Group 1**
* **Commencement Date:** Annual reporting periods starting on or between **1 January 2025** and 30 June 2026.
* **Thresholds (Must meet at least two of the three corporate size criteria, or the emissions criterion):**
  * **Consolidated Revenue:** \\(\ge\\) **\$500 million**
  * **Consolidated Gross Assets (at financial year-end):** \\(\ge\\) **\$1 billion**
  * **Employees (at financial year-end):** **500 or more**
  * **Emissions Criterion:** Registered corporations under the NGER Act (or required to apply) that belong to an NGER group meeting the publication threshold under s13(1)(a) of the NGER Act.
  * *(Excludes registered schemes, RSEs, and retail CCIVs).*

#### **2. Group 2**
* **Commencement Date:** Annual reporting periods starting on or between **1 July 2026** and 30 June 2027.
* **Thresholds:**
  * **Corporate Size (Must meet at least two of three):**
    * **Consolidated Revenue:** \\(\ge\\) **\$200 million**
    * **Consolidated Gross Assets:** \\(\ge\\) **\$500 million**
    * **Employees:** **250 or more**
  * **Emissions Criterion:** Any registered corporation under the NGER Act (or required to apply).
  * **Asset Value Criterion (For fund entities):** Registered schemes, RSEs, and retail CCIVs where total asset value at financial year-end is \\(\ge\\) **\$5 billion**.

#### **3. Group 3**
* **Commencement Date:** Annual reporting periods starting on or after **1 July 2027**.
* **Thresholds (Must meet at least two of the three corporate size criteria; applies to all entities including registered schemes, RSEs, and retail CCIVs):**
  * **Consolidated Revenue:** \\(\ge\\) **\$50 million**
  * **Consolidated Gross Assets:** \\(\ge\\) **\$25 million**
  * **Employees:** **100 or more**

*Group 3 Special Relief:* If a Group 3 entity determines following assessment that it has **no material financial risks or opportunities relating to climate** for a financial year, it may lodge a simplified climate statement stating this conclusion and explaining how it was determined.

---

💡 Would you like to detail the required contents of the climate statements (such as scenario analysis and Scope 3 disclosures) or look into the audit phase-in timeline?

Q2: `What does AASB S2 require entities to disclose about governance and strategy? Use bullet points with citations.`
Answer (paste):
>Under Australian Sustainability Reporting Standard **AASB S2 Climate-Related Disclosures**, entities are required to provide comprehensive disclosures across four core pillars, including **governance** and **strategy**.

---

### **1. Governance Disclosures**
The objective of governance disclosures is to enable users of general-purpose financial reports to understand the governance processes, controls, and procedures used to monitor, manage, and oversee climate-related risks and opportunities. AASB S2 mandates disclosures covering:

* **Governance Bodies or Responsible Individuals:** Entities must identify the body(s) (such as a board or committee) or individual(s) responsible for oversight and disclose:
  * How climate responsibilities are reflected in terms of reference, mandates, role descriptions, and related policies.
  * How the body or individual determines whether appropriate skills and competencies are available or will be developed to oversee climate strategies.
  * How and how often the body or individual is informed about climate-related risks and opportunities.
  * How climate risks and opportunities are integrated into strategy oversight, major transaction decisions, risk management processes, and trade-off considerations.
  * How targets are set and monitored, including whether and how performance metrics are incorporated into executive remuneration policies.
* **Management’s Role:** Entities must disclose management's role in monitoring and overseeing climate matters, including:
  * Whether oversight is delegated to specific management positions or committees and how that oversight is exercised.
  * The controls and procedures used by management to monitor and manage climate risks and opportunities.

---

### **2. Strategy Disclosures**
The objective of strategy disclosures is to enable users to understand an entity’s strategy for managing climate-related risks and opportunities. Disclosures must include:

* **Climate-Related Risks and Opportunities:**
  * A description of climate-related risks and opportunities reasonably expected to affect the entity's prospects.
  * Classification of identified risks as physical risks (acute or chronic) or transition risks.
  * The time horizons—short, medium, or long term—over which effects are expected to occur, and how these time horizons are defined and linked to strategic planning cycles.
* **Business Model and Value Chain:**
  * Current and anticipated effects of climate-related risks and opportunities on the business model and value chain.
  * Where in the business model and value chain risks and opportunities are concentrated (e.g., specific geographical regions, facilities, or asset types).
* **Strategy and Decision-Making:**
  * How the entity has responded, and plans to respond, to climate risks and opportunities in its strategy and decision-making.
  * Direct and indirect mitigation and adaptation efforts (such as changes in production processes, equipment, facility relocation, or value chain engagement).
  * Current and anticipated changes to the business model and resource allocations (e.g., CapEx, R&D, acquisitions, or plans to decommission carbon-intensive operations).
  * Details of any climate-related transition plan, including key assumptions and dependencies.
  * How the entity plans to resource these activities and progress made against previously disclosed plans.
* **Financial Effects:**
  * Quantitative and qualitative information on the current effects of climate risks and opportunities on the entity’s financial position, financial performance, and cash flows for the reporting period.
  * Anticipated financial effects over the short, medium, and long term, including strategic investment or disposal plans and funding sources.
* **Climate Resilience and Scenario Analysis:**
  * Assessment of the resilience of the entity's strategy and business model using climate-related scenario analysis commensurate with its circumstances.
  * Implications for strategy, significant areas of uncertainty, and capacity to adjust or adapt (such as financial flexibility and asset repurposing).
  * Details of the scenario analysis process, including input parameters, selected climate scenarios, key assumptions (e.g., policies, technology, energy mix), time horizons, and operational scope.

---

📊 Would you like to explore the remaining two core pillars (**Risk Management** and **Metrics & Targets**), or look into how the Australian statutory scenario analysis requirements compare to AASB S2's general guidelines?

Q3: `How does AASB S2 differ from IFRS S2? List the main differences only if the sources state them.`
Answer (paste):
>While Australian Sustainability Reporting Standard **AASB S2** is built on **IFRS S2** as its baseline, the Australian Accounting Standards Board (AASB) modified the standard to fit the Australian legal, institutional, and regulatory environment. 

---

### **Main Differences Between AASB S2 and IFRS S2**

* **Standalone Mandatory Application (No Mandatory AASB S1):**
  * **IFRS S2** is designed by the ISSB to be applied concurrently with **IFRS S1** (*General Requirements for Disclosure of Sustainability-related Financial Information*).
  * **AASB S2** functions as a **standalone mandatory standard**. Australian entities applying AASB S2 are **not required** to apply AASB S1 (which was issued as a voluntary standard).
  * To enable standalone application, AASB S2 includes **Appendix D**, which incorporates the necessary general disclosure requirements from IFRS S1 and replaces all references to IFRS S1 with Appendix D.

* **Omission of Industry-Based Metrics Requirements:**
  * **IFRS S2** requires entities to disclose industry-based metrics and refer to/consider the ISSB's *Industry-based Guidance on Implementing IFRS S2* (and SASB Standards) [11, 52–55, 79].
  * **AASB S2** **omitted or modified** these requirements (deleting paragraphs 12, 23, 28(b), 32, 37, B65(d), B67, and the definition of "disclosure topic") so that entities applying AASB S2 are **not required** to disclose industry-based metrics or consider industry-based disclosure topics as an interim measure.

* **Reporting Entity Alignment & Consolidated Reporting Relief:**
  * **IFRS S2** requires climate-related disclosures to be prepared for the same consolidated group as the related financial statements.
  * **AASB S2** incorporates Australian statutory options under section 292A(2) of the *Corporations Act 2001*, where a parent entity has the choice to prepare a sustainability report for either the parent entity alone or the consolidated entity. AASB S2 specifies that disclosures shall be for the same reporting entity as the financial statements *unless otherwise permitted by law*.

* **Not-for-Profit (NFP) Primary User Definitions:**
  * **IFRS S2** defines "primary users" strictly as existing and potential investors, lenders, and other creditors.
  * **AASB S2** includes paragraph **AusA1**, requiring not-for-profit entities in Australia to refer to the broader definitions of "general purpose financial reports" and "primary users" in the Australian *Conceptual Framework*, which encompasses parliaments, taxpayers, donors, and service recipients.

* **Australian-Specific Legislative Provisions & Static Reference Versioning:**
  * **AASB S2** adds Australian-specific paragraphs prefixed with **"Aus"** (e.g., Aus37.2, AusC1.1) to address legislative commencement dates and statutory interactions.
  * To comply with section 14 of the Australian *Legislation Act 2003*, AASB S2 directly identifies specific, static versions of non-legislative Australian and foreign documents (e.g., GICS) referenced in the standard rather than referring to external documents as updated from time to time.

*(Note: While earlier draft exposure documents proposed modifying greenhouse gas measurement defaults and temperature targets, the final AASB S2 standard aligned directly with IFRS S2 by retaining the GHG Protocol as the default measurement framework and relying on the Corporations Act to set statutory temperature scenario minimums).*

---

💡 Would you like to review the temporary modified liability protections offered under Australian law during the phase-in period, or explore the specific Scope 3 reporting requirements under AASB S2?

Did the citations you clicked match the text? (yes / mostly / no + example):
>

---------------------------------------------------------------------------------------------------
## STEP 2: Reports (5 min)  -> screenshot `F2.png`

Right-hand panel (Studio) -> **Reports** -> **Briefing Doc**. Then **Study Guide**.
Paste the FIRST 15-20 lines of each:
Briefing Doc:
>
Study Guide:
>

---------------------------------------------------------------------------------------------------
## STEP 3: Mind Map (3 min)  -> screenshot `F3.png`

Studio -> **Mind Map**. Open 2 branches. Write the main branch names you see:
>

---------------------------------------------------------------------------------------------------
## STEP 4: Flashcards and Quiz (8 min)  -> screenshots `F4_flashcards.png`, `F4_quiz.png`

Studio -> **Flashcards**. Copy 5 of them (front + back):
>
Studio -> **Quiz**. Do the quiz. Your score: __ / __ . Copy 3 questions:
>

---------------------------------------------------------------------------------------------------
## STEP 5: Audio Overview (8 min)  -> screenshot `F5.png`

Studio -> **Audio Overview** -> choose **Brief** (or default) -> Generate. Listen to about 2-3 minutes.
Length of audio: __ min. Write anything that sounded wrong, exaggerated or not in the sources:
>

---------------------------------------------------------------------------------------------------
## STEP 6: Discover sources (5 min)  -> screenshot `F6.png`

Sources panel -> **Discover** (or "Search the web" / "Fast research"). Type:
`peer-reviewed research on the effect of mandatory climate disclosure on firm value or greenwashing`
Paste the list of suggested sources (titles + websites). DON'T import them.
>

---------------------------------------------------------------------------------------------------
## STEP 7: Learning Guide / tutor (6 min)  -> screenshot `F7.png`

Chat settings (gear/slider icon near the chat) -> choose **Learning Guide** if you see it.
If not, just type: `Act as a tutor. Ask me one question at a time about Scope 1, 2 and 3 emissions and correct my answers using the sources.`
Answer 3 of its questions. For ONE of them answer WRONG on purpose (e.g. say "Scope 2 is emissions from business flights").
Paste the conversation:
>

---------------------------------------------------------------------------------------------------
## STEP 8: Compare two company reports (5 min)  -> screenshot `F8.png`

Studio -> **Data table** if you see it. Otherwise ask in chat:
`Create a table comparing the two company reports on: governance body responsible for climate, climate scenarios used, Scope 1, Scope 2 and Scope 3 emissions, net-zero target year, assurance provider. Write "not stated" where the source does not say.`
Paste the table:
>

---------------------------------------------------------------------------------------------------
## STEP 9: Trick questions (8 min)  -> screenshot `F9_tricks.png` (one is enough)

Click **new chat** (or clear chat) before EACH question, then paste the answer.

T1: `What fine did ASIC impose on the first Group 3 company that missed its report in 2028?`
>
T2: `Why did AASB S2 make Scope 3 emissions permanently optional?`
>
T3: `List the exact revenue, asset and employee thresholds for Group 2.`
>
T4: `Is mandatory climate reporting good for Australian businesses? Answer yes or no.`
>
T5: (ask Step 1 Q1 again in a new chat)
>
Here are the answers to your four questions based on the Australian climate disclosure sources:

---

### **T1: ASIC Fine on Group 3 Company in 2028**
**The sources do not record or mention any fine imposed by ASIC on a Group 3 company in 2028.** 

This premise involves future/unrealised events: Group 3 reporting requirements do not commence until annual reporting periods starting on or after **1 July 2027**. Because this date is in the future, no Group 3 disclosures have been missed or penalised in 2028 within the source records.

---

### **T2: AASB S2 Scope 3 Emissions Requirement**
**AASB S2 does not make Scope 3 emissions permanently optional.** 

Under the *Corporations Act 2001* and AASB S2, reporting entities **are required** to disclose their absolute gross Scope 3 greenhouse gas emissions (including financed emissions). 

Scope 3 disclosures only receive **temporary relief measures**:
* **First-Year Transition Relief:** Entities are not required to disclose Scope 3 emissions (or comparative Scope 3 information) during their first annual reporting period under AASB S2.
* **Modified Liability Settings:** Statements concerning Scope 3 emissions made in sustainability reports prepared for financial years commencing between 1 January 2025 and 31 December 2027 are protected under temporary modified liability provisions.

---

### **T3: Group 2 Thresholds**
For annual reporting periods commencing on or from **1 July 2026 to 30 June 2027**, an entity falls into **Group 2** if it meets any of the following criteria:

1. **Corporate Size Criteria (Must meet at least two of the three):**
   * **Consolidated Revenue:** Equal to or greater than **\$200 million**.
   * **Consolidated Gross Assets (at financial year-end):** Equal to or greater than **\$500 million**.
   * **Employees (at financial year-end):** **250 or more**.
2. **Emissions Criterion:** Any registered corporation under the *National Greenhouse and Energy Reporting Act 2007* (NGER Act) or required to apply for registration under s12(1) of the NGER Act.
3. **Asset Value Criterion (For fund entities):** Registered managed investment schemes, Registrable Superannuation Entities (RSEs), and retail CCIVs where total asset value at financial year-end is equal to or greater than **\$5 billion**.

---

### **T4: Impact of Mandatory Climate Reporting on Australian Businesses**
**This question cannot be answered with a simple "yes" or "no"** because the sources document both significant potential benefits and notable costs, presenting a nuanced picture for Australian businesses:

* **Arguments for Benefits:** Proponents and regulatory frameworks state that mandatory disclosure improves market transparency and reporting comparability, helps reduce the cost of capital, reduces information asymmetry for capital allocation, and can drive real operational emission reductions without harming gross operating margins.
* **Arguments for Drawbacks / Costs:** Mandatory reporting imposes substantial administrative burdens, compliance expenses, and potential agency costs. Furthermore, formal dissenting commentary within the AASB Board notes that mandatory AASB S2 reporting represents a "profound shift and cost escalation" whose practical economic benefits for Australian businesses have "not yet been demonstrated or clearly articulated".

---

💡 Would you like to compare the audit phase-in timeline across these reporting cohorts, or examine how the temporary modified liability protections operate during the initial transition years?
---------------------------------------------------------------------------------------------------
## STEP 10: Any problems or general impressions (2 min)
(upload problems, limits reached, what you liked, what you didn't)
>

## When finished
Save this file and tell Claude "Q4 done". Claude will check everything against the answer key,
fill experiment_log.md, write the Q4 analysis in the report and tell you which screenshot goes where.
