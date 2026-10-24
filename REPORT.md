# Graduation Project Report: Week 1 Draft

## 1. Introduction
The integration of computer vision into healthcare represents a major advancement for clinical diagnostics. Modern medical software harnesses automated algorithms to process intricate biological images, providing vital assistance to medical staff before complex procedures take place.

## 2. Problem Statement
Ophthalmic clinics often face workflow bottleneck during preoperative evaluations. When human eyes manually inspect retinal scans for microscopic lesions, the process is slow and prone to oversight, risking unflagged pathologies prior to surgery.

## 3. Motivation
Protecting human vision from surgical complications demands absolute precision. Ensuring that the scalpel never meets an unprepared eye makes automated, reliable secondary screening an essential safety measure for modern medicine.

## 4. Project Objective
This project aims to develop a clinical decision-support application powered by object detection algorithms. The software will automatically analyze retinal images, isolate specific anomalies, and present clear visual indicators to support clinical clearance workflows.

## 5. Preliminary Scope
* **Included in Version 1:** Core image processing logic, YOLOv8 object detection pipelines, a FastAPI backend service, and a local mock database supporting basic patient record management.
* **Excluded from Version 1:** Live interoperability protocols connecting directly to hospital Electronic Health Record systems, as well as multi-disease diagnostic modules other than diabetic retinopathy markers.

## 6. Requirements Analysis
The primary users of this system are ophthalmic surgeons and clinical triage technicians. The core problem they face is the operational bottleneck of manually screening retinal fundus images for microscopic pre-surgical contraindications[cite: 11]. The single most important result this project will deliver is a rapid, automated secondary visual assessment[cite: 11].

## 7. Functional Requirements
| ID | Requirement statement | Priority |
| :--- | :--- | :--- |
| FR-01 | The system shall allow a user to upload a digital fundus image file. | Must |
| FR-02 | The system shall process the uploaded image via a YOLOv8 object detection model. | Must |
| FR-03 | The system shall display the image with bounding boxes indicating anomalies. | Must |
| FR-04 | The system shall calculate and display a pre-surgical risk score based on detections. | Should |
| FR-05 | The system shall allow users to save the diagnostic output to a local patient profile. | Should |

## 8. Non-Functional Requirements
| ID | Quality | Requirement | How to verify |
| :--- | :--- | :--- | :--- |
| NFR-01 | Performance | The API shall return inference results within 5 seconds of image upload. | Measure response time with a 224x224 test image. |
| NFR-02 | Validation | The system shall reject non-image file uploads with a specific error message. | Attempt to upload a .pdf and verify the rejection prompt. |

## 9. Project Scope, Constraints, and Assumptions
| Category | Question | Project Specification |
| :--- | :--- | :--- |
| In scope | What will the first version include? | Detection of diabetic retinopathy markers via bounding boxes. |
| Out of scope | What is intentionally postponed? | Integration with live hospital HL7/FHIR EHR networks. |
| Constraint | What limits development? | AI model must be trained in the cloud due to local hardware limits. |
| Assumption | What are you relying on? | The clinical workstation has internet access to reach the FastAPI backend. |

## 10. Use Cases and User Stories
**User Story 1 (Linked to FR-03):** 
As an ophthalmic surgeon, I want to view bounding boxes over retinal lesions so that I can instantly verify the AI's diagnostic reasoning.
* **Acceptance Criterion 1:** Given a processed image, bounding boxes are clearly drawn around detected anomalies.
* **Acceptance Criterion 2:** Each bounding box displays a visible confidence percentage.

**User Story 2 (Linked to FR-01):** 
As a clinical screening technician, I want to upload a patient's fundus scan into the system so that it can be evaluated before the surgeon's review.
* **Acceptance Criterion 1:** When I select a valid JPEG/PNG image, the system successfully initiates the upload to the API.
* **Acceptance Criterion 2:** When the upload begins, a loading indicator appears while waiting for inference.

## 11. Development Plan
| Week | Expected milestone in the nine-week program |
| :--- | :--- |
| Week 3 | System architecture diagrams mapping the frontend to the FastAPI/YOLOv8 backend. |
| Week 4 | First demonstrable prototype allowing image upload via API and returning a basic text response. |
| Week 5 | Integration of the trained YOLOv8 model into the API for live bounding box generation. |
| Week 6 | Execution of validation tests comparing AI outputs against the ground-truth dataset labels. |
| Week 7 | Finalization of UI integration with Firebase mock patient records. |
| Week 8 | Report completion and professional README with software installation instructions. |
| Week 9 | Final demonstration of end-to-end image upload, API inference, and UI risk assessment. |
