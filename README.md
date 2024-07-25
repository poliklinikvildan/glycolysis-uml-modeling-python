
## Overview

Description:
This repository provides a detailed use case modeling of the glycolysis pathway using Unified Modeling Language (UML) and Python. It identifies the key enzymes (actors) involved in glycolysis, their goals, and the biochemical reactions (use cases) they catalyze. The project includes Python code to generate UML diagrams that visually represent the enzymatic steps of glycolysis, facilitating a clearer understanding of this essential biochemical pathway. This integration of software engineering principles with biochemistry offers an educational tool for students and licensed professionals in both fields.
# Glycolysis Pathway Analysis

## Table of Contents

1. [Introduction](#introduction)
2. [Use Case Modeling](#use-case-modeling)
3. [Operation Contracts](#operation-contracts)
4. [UML Diagrams](#uml-diagrams)
5. [Installation and Usage](#installation-and-usage)
6. [Contributing](#contributing)
7. [License](#license)

## Introduction

Glycolysis is a crucial metabolic pathway that converts glucose into pyruvate while producing ATP and NADH. This repository aims to provide an in-depth look at the glycolysis pathway, modeling each enzymatic step as use cases and operations.

## Use Case Modeling

### Actors

- **Hexokinase**
- **Phosphoglucose Isomerase**
- **Phosphofructokinase-1**
- **Aldolase**
- **Triose Phosphate Isomerase**
- **Glyceraldehyde-3-Phosphate Dehydrogenase**
- **Phosphoglycerate Kinase**
- **Phosphoglycerate Mutase**
- **Enolase**
- **Pyruvate Kinase**

### Use Cases

1. **Phosphorylation of Glucose**: Hexokinase catalyzes the phosphorylation of glucose to form glucose-6-phosphate.
2. **Isomerization of Glucose-6-Phosphate**: Phosphoglucose isomerase converts glucose-6-phosphate into fructose-6-phosphate.
3. **Phosphorylation of Fructose-6-Phosphate**: Phosphofructokinase-1 phosphorylates fructose-6-phosphate to form fructose-1,6-bisphosphate.
4. **Cleavage of Fructose-1,6-Bisphosphate**: Aldolase cleaves fructose-1,6-bisphosphate into two three-carbon molecules.
5. **Isomerization of Dihydroxyacetone Phosphate**: Triose phosphate isomerase converts dihydroxyacetone phosphate into glyceraldehyde-3-phosphate.
6. **Oxidation and Phosphorylation of Glyceraldehyde-3-Phosphate**: Glyceraldehyde-3-phosphate dehydrogenase catalyzes the oxidation of glyceraldehyde-3-phosphate.
7. **Substrate-Level Phosphorylation to Produce ATP**: Phosphoglycerate kinase produces ATP through substrate-level phosphorylation.
8. **Rearrangement of 3-Phosphoglycerate**: Phosphoglycerate mutase converts 3-phosphoglycerate to 2-phosphoglycerate.
9. **Dehydration of 2-Phosphoglycerate**: Enolase dehydrates 2-phosphoglycerate to produce phosphoenolpyruvate.
10. **Substrate-Level Phosphorylation to Produce Pyruvate**: Pyruvate kinase converts phosphoenolpyruvate to pyruvate, generating ATP.

## Operation Contracts

Each use case includes specific operation contracts that define the preconditions and postconditions of the enzymatic reactions:

- **Phosphorylation of Glucose**: Hexokinase catalyzes the conversion of glucose to glucose-6-phosphate using ATP.
- **Isomerization of Glucose-6-Phosphate**: Phosphoglucose isomerase converts glucose-6-phosphate to fructose-6-phosphate.
- **Phosphorylation of Fructose-6-Phosphate**: Phosphofructokinase-1 catalyzes the conversion of fructose-6-phosphate to fructose-1,6-bisphosphate using ATP.
- **Cleavage of Fructose-1,6-Bisphosphate**: Aldolase splits fructose-1,6-bisphosphate into two three-carbon molecules.
- **Isomerization of Dihydroxyacetone Phosphate**: Triose phosphate isomerase converts dihydroxyacetone phosphate into glyceraldehyde-3-phosphate.
- **Oxidation and Phosphorylation of Glyceraldehyde-3-Phosphate**: Glyceraldehyde-3-phosphate dehydrogenase oxidizes glyceraldehyde-3-phosphate and phosphorylates it.
- **Substrate-Level Phosphorylation to Produce ATP**: Phosphoglycerate kinase generates ATP from ADP and 1,3-bisphosphoglycerate.
- **Rearrangement of 3-Phosphoglycerate**: Phosphoglycerate mutase converts 3-phosphoglycerate to 2-phosphoglycerate.
- **Dehydration of 2-Phosphoglycerate**: Enolase converts 2-phosphoglycerate to phosphoenolpyruvate by removing water.
- **Substrate-Level Phosphorylation to Produce Pyruvate**: Pyruvate kinase converts phosphoenolpyruvate to pyruvate, producing ATP.

## References

**Biochemistry Textbooks**:
   - Berg, J. M., Tymoczko, J. L., & Gatto, G. J. (2012). *Biochemistry* (7th ed.). W.H. Freeman and Company.
   - Nelson, D. L., Cox, M. M. (2017). *Lehninger Principles of Biochemistry* (7th ed.). W.H. Freeman and Company.

**Online Resources**:
   - [NCBI Glycolysis Overview](https://www.ncbi.nlm.nih.gov/books/NBK2264/)
   - [KEGG Pathway Database](https://www.genome.jp/kegg/pathway.html)

**UML Modeling References**:
   - Bell, D. (2003). An introduction to the Unified Modeling Language. IBM DeveloperWorks. [Link](https://www.ibm.com/developerworks/rational/library/content/RationalEdge/jul2003/edge2/)
   - Sparx Systems. UML Tutorial - Unified Modelling Language. [Link](https://www.sparxsystems.com/resources/uml2/index.html)

**Tools Used**:
   - PyDot for generating UML diagrams: [PyDot Documentation](https://github.com/pydot/pydot)
   - Graphviz for rendering: [Graphviz Documentation](https://graphviz.gitlab.io/documentation/)

## UML Diagrams

Detailed UML diagrams representing the glycolysis pathway are included in this repository. These diagrams illustrate the interactions between enzymes and the transformations of metabolites through glycolysis.

## Installation and Usage

To view the UML diagrams and other files in this repository, clone or download the repository:

```bash
git clone https://github.com/yourusername/glycolysis-pathway-analysis.git


### Key Points
- **Actors**: Represent enzymes in glycolysis.
- **Operations**: The biochemical transformations catalyzed by each enzyme.
- **Preconditions**: Requirements before an operation can occur.
- **Postconditions**: Outcomes after an operation is completed.



