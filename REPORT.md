# Graduation Project Report: Week 1 Draft

## Introduction
The integration of computer vision into healthcare represents a major advancement for clinical diagnostics. Modern medical software harnesses automated algorithms to process intricate biological images, providing vital assistance to medical staff before complex procedures take place.

## Problem Statement
Ophthalmic clinics often face workflow bottleneck during preoperative evaluations. When human eyes manually inspect retinal scans for microscopic lesions, the process is slow and prone to oversight, risking unflagged pathologies prior to surgery.

## Motivation
Protecting human vision from surgical complications demands absolute precision. Ensuring that the scalpel never meets an unprepared eye makes automated, reliable secondary screening an essential safety measure for modern medicine.

## Project Objective
This project aims to develop a clinical decision-support application powered by object detection algorithms. The software will automatically analyze retinal images, isolate specific anomalies, and present clear visual indicators to support clinical clearance workflows.

## Preliminary Scope
* **Included in Version 1:** Core image processing logic, YOLOv8 object detection pipelines, a FastAPI backend service, and a local mock database supporting basic patient record management.
* **Excluded from Version 1:** Live interoperability protocols connecting directly to hospital Electronic Health Record systems, as well as multi-disease diagnostic modules other than diabetic retinopathy markers.
