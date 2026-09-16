test:
	python -m unittest discover -s tests -v

run:
	uvicorn app.main:app --reload

docker-up:
	docker compose up --build

cycle:
	python scripts/run_cycle.py "Explore a new reflective memory pattern"
