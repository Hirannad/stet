.PHONY: check hooks

check:
	@python3 scripts/check.py

hooks:
	@git config core.hooksPath .githooks
	@echo "pre-commit hook installed (core.hooksPath=.githooks)"
