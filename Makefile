.PHONY: check runs hooks

check:
	@python3 scripts/check.py

# Parses every recorded run against the output shape SKILL.md specifies. Silent no-op until
# tests/corpus/runs/ has something in it, so a fresh clone does not fail on an empty directory.
runs:
	@if ls tests/corpus/runs/*.md >/dev/null 2>&1; then \
		python3 scripts/parse_run.py --strict tests/corpus/runs/*.md; \
	else \
		echo "no recorded runs in tests/corpus/runs/ — nothing to parse"; \
	fi

hooks:
	@git config core.hooksPath .githooks
	@echo "pre-commit hook installed (core.hooksPath=.githooks)"
