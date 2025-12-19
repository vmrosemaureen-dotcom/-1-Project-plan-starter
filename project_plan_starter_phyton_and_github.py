# project_plan.py
# Starter Project Plan with GitHub and Python

project_plan = {
    "overview": {
        "project_topic": "Starter Project with GitHub and Python",
        "owner": "",        
        "duration": "",     
        "audience": ""      
    },
    "objectives": {
        "primary": "Establish a reproducible starter workflow using Python and GitHub",
        "secondary": [
            "Practice version control basics (commit, branch, pull request)",
            "Set up Python environment with dependencies",
            "Document project structure for future reuse"
        ]
    },
    "research_questions": {
        "primary": "How can GitHub and Python be combined to create a clean, reusable starter project?",
        "secondary": [
            "What files and folders are essential for a Python starter repo?",
            "How can .gitignore and README improve reproducibility and onboarding?"
        ]
    },
    "milestones": [
        {"name": "Initialization and Setup", "tasks": ["create repo", "add README.md", "add .gitignore"]},
        {"name": "Environment Setup", "tasks": ["create venv/conda", "add requirements.txt"]},
        {"name": "Project Structure", "tasks": ["create folders: data/, scripts/, notebooks/, models/"]},
        {"name": "Version Control Practice", "tasks": ["commit starter files", "create branch", "open PR"]},
        {"name": "Documentation", "tasks": ["update README.md", "add checklist"]},
        {"name": "Review and Handover", "tasks": ["finalize project plan", "close issues", "merge PRs"]}
    ],
    "deliverables": [
        "README.md with checklist",
        "project_plan.md",
        ".gitignore",
        "requirements.txt",
        "starter folders"
    ],
    "acceptance_criteria": [
        "Repo contains clear structure and starter files",
        "Python environment reproducible via requirements.txt",
        "GitHub workflow demonstrated with commits, branch, and PR",
        "Documentation explains how to start using the repo"
    ],
    "checklist": [
        "Create GitHub repository",
        "Add README.md and project_plan.md",
        "Add .gitignore",
        "Set up virtual environment",
        "Add requirements.txt",
        "Create starter folders",
        "Commit and push changes",
        "Create branch and open PR",
        "Update documentation and close issues"
    ]
}

if __name__ == "__main__":
    # Print plan summary
    print("=== Project Plan Starter ===")
    for section, content in project_plan.items():
        print(f"\n{section.upper()}:")
        print(content)
