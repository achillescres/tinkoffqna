.PHONY: all
all:
	uvicorn app.main:app --reload

.PHONY: i
i:
	pip install -r requirements.txt
