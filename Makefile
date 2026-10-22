.PHONY: day week stats test lab ml-lab platform-test

day:
	python scripts/forge.py new-day

week:
	python scripts/forge.py week

stats:
	python scripts/forge.py stats

test:
	pytest -q

# make lab LAB=lab01_log_analyzer   (searches python/labs and ml/labs)
lab:
	@d=$$(ls -d python/labs/$(LAB) ml/labs/$(LAB) 2>/dev/null | head -1); \
	test -n "$$d" || (echo "unknown lab"; exit 1); \
	cd $$d && python -m pytest -q

platform-test:
	cd nse_platform && python -m pytest -q
