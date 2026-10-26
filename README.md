# AI-Assisted Retinal Anomaly Detection System for Ophthalmic Pre-Surgical Screening

## Project Description
Before elective eye procedures like LASIK or cataract removal, the medical team must verify the health of the retina. Undiagnosed conditions such as diabetic retinopathy can lead to severe postoperative complications. Currently, manual screening of fundus images creates a heavy diagnostic bottleneck for the clinic. This software provides an automated solution by analyzing retinal scans to flag micro-aneurysms and lesions before surgical clearance.

## Objective
To develop a clinical decision-support application powered by a computer vision model that automatically detects and localizes retinal anomalies, providing the medical staff with an instant diagnostic risk assessment.

## Target Users
* Ophthalmic surgeons
* Clinical screening technicians
* Hospital triage staff managing preoperative workflows

## Planned Features
* Digital fundus image upload and processing
* Automated YOLOv8 object detection for diabetic retinopathy lesions
* Visual bounding box annotations with confidence scores
* Pre-surgical risk score calculation
* Local patient profile management

## Scope
* **In Scope:** Detection of diabetic retinopathy markers via bounding boxes; standalone clinical frontend app with a local mock database.
* **Out of Scope:** Integration with live hospital HL7/FHIR EHR networks; detection of non-retinal diseases.

## Current Status
Week 3: Architecture and Technical Design
