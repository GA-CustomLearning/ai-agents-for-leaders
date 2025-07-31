# Example Governance Checklist

This is an example of a completed governance checklist, demonstrating how you might fill it out for a hypothetical AI agent project.

- **Data Privacy & Compliance**
  - Is PII handled securely? **Yes, all PII is encrypted at rest and in transit using AES-256.**
  - Does the workflow adhere to GDPR/CCPA? **Yes, data processing agreements are in place and audited quarterly.**

- **Human-in-the-Loop**
  - Who reviews AI outputs before action? **All critical AI-generated recommendations are reviewed by a human subject matter expert before implementation.**
  - What escalation paths exist? **If a recommendation is flagged, it goes to the project lead, then to the legal/compliance team if unresolved.**

- **Bias & Fairness**
  - Have you assessed potential biases? **Initial bias assessment completed using Aequitas, identified potential bias in customer segmentation for marketing recommendations.**
  - Is there a mitigation plan? **Yes, implementing re-sampling techniques and monitoring for disparate impact in A/B tests.**

- **Security & Access**
  - Are API keys & credentials stored safely? **All API keys are stored in Azure Key Vault with least privilege access.**
  - Who has access to the agent? **Only authorized development and operations personnel have access, managed via Azure AD groups.**

- **Audit & Logging**
  - Are all actions logged? **Yes, all AI agent actions and decisions are logged to Azure Monitor for auditing.**
  - Is there a review cadence? **Logs are reviewed weekly by the operations team and monthly by the compliance team.**