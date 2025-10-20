# deepfake-detector
University of Plymouth – COMP3000 Final Year Project Deepfake Detection using AI for Cybersecurity (Supervisor: Dr Bogdan Ghita)
Timeline (Simplified)
| Phase | Date | Deliverable |
|-------|------|--------------|
| Supervisor Selection | Oct 10 | Confirmed supervisor |
| Project Initiation | Oct 24 | Vision, Risk Assessment, Gantt |
| Poster Draft | Mar 16 | Poster feedback |
| Poster Final | Apr 20 | Final print |
| Report + Demo | May 5 | ePortfolio Submission |
| Viva | w/c May 11 | Oral Defence |



| Risk | Probability | Impact | Mitigation |
|------|--------------|---------|-------------|
| GPU limitations | Medium | High | Use Colab Pro / UoP GPU servers |
| Dataset bias | Medium | Medium | Use multiple datasets, document limitations |
| Overfitting | Medium | High | Apply augmentations, regularisation |
| Time pressure | Medium | High | Weekly progress in Trello |
| Ethical misuse | Low | High | Defensive research only, disclaimers |



deepfake-detector/
├── README.md
├── requirements.txt
├── configs/
├── src/
│ ├── preprocessing/
│ ├── models/
│ ├── datasets/
│ └── utils/
├── scripts/
│ ├── train.py
│ ├── eval.py
│ └── inference.py
├── app/
│ ├── main.py
│ └── templates/
└── tests/
