export DOCKER_HOST ?= unix://$(HOME)/.colima/default/docker.sock

.PHONY: test report clean

test:
	python3 -m unittest discover -s tests -t . -v

report:
	python3 bench.py report results

clean:
	rm -rf $(HOME)/.cache/boundary-bench
