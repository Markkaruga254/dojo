# Lab 04: Terraform workflow without cloud spend

## Outcome

Practise Terraform's init, fmt, validate, plan, apply, and destroy lifecycle using a local file resource. This teaches state and review discipline without creating billable cloud infrastructure.

## Prerequisites

- Terraform CLI installed from the official HashiCorp distribution.
- A new, isolated working directory outside a production project.
- No cloud credentials are required or should be configured for this exercise.

## Task 1 — Define a local resource

Create a main.tf that declares the Terraform and local-provider requirements and manages one text file under a lab output directory. The content should be harmless and contain no secrets or personal data. Use variables for the filename/content if you want the extra practice.

Keep the resource path inside the lab directory. Do not use absolute paths that point to system files or existing user documents.

## Task 2 — Format, validate, and plan

Run the following from the lab directory:

    terraform fmt -check
    terraform init
    terraform validate
    terraform plan -out=tfplan

Review the plan before applying it. Confirm that it will only create or update the intended lab file. If the plan includes unrelated paths or resources, stop and fix the configuration. Do not commit tfplan or Terraform state.

## Task 3 — Apply and destroy

Only after reviewing the plan:

    terraform apply tfplan
    cat output/lab.txt
    terraform state list
    terraform destroy

Confirm the generated file is removed and the state reports no managed resources. If any command fails, inspect the error and state before retrying; do not delete state blindly.

## State and Git hygiene

Add these exclusions to the isolated lab's .gitignore:

    .terraform/
    *.tfstate
    *.tfstate.*
    tfplan
    crash.log
    crash.*.log

Commit the configuration and a sanitized explanation, not state, plan files, credentials, or generated output unless the task explicitly requires a harmless fixture. Do not put secrets in Terraform variables or outputs.

## Exit criteria

- [ ] terraform fmt -check, init, and validate succeed.
- [ ] Plan shows only the intended local resource.
- [ ] Apply creates the expected harmless file.
- [ ] Destroy removes the managed file.
- [ ] State and plan artifacts are excluded from Git.
- [ ] Record the plan/apply/destroy sequence and one failure mode.

## Explain

1. What does Terraform state track, and why is it sensitive?
2. Why review a plan before apply?
3. What is the difference between a provider and a resource?
4. What additional controls would be required before using a cloud provider?

This is not a cloud deployment. Do not describe it as one.
