.PHONY: check runs fixtures cache hooks

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

# Checks the tests/fixtures/ specifications against the catalogue, always, and compares any run
# recorded under tests/fixtures/runs/ against the fixture it was produced from. It reports which
# of the two it did — an arm that could not fire must not read like one that fired and found
# nothing.
fixtures:
	@python3 scripts/check_fixtures.py

# Which catalogue a Skill-tool run reads: this working copy, or the installed plugin. Round 3
# found the two had drifted, so measuring through the Skill tool measured the release instead —
# silently, with plausible output. Fails when they differ, and names the copy behind every
# recorded run. Local only: CI has no installed plugin, and this is a fact about a machine at a
# moment rather than a property of a commit.
cache:
	@if ls tests/corpus/runs/*.md >/dev/null 2>&1; then \
		python3 scripts/plugin_cache.py tests/corpus/runs/*.md; \
	else \
		python3 scripts/plugin_cache.py; \
	fi

hooks:
	@git config core.hooksPath .githooks
	@echo "pre-commit hook installed (core.hooksPath=.githooks)"
