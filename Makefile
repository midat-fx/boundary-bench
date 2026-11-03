IMAGE := $(shell python3 -c 'import bench; print(bench.IMAGE)')

# colima's socket, only on machines that have colima; elsewhere docker's default is right.
ifneq ($(wildcard $(HOME)/.colima/default/docker.sock),)
export DOCKER_HOST ?= unix://$(HOME)/.colima/default/docker.sock
endif

.PHONY: test sandbox-image report clean

test:
	python3 -m unittest discover -s tests -t . -v

# Without the image the sandbox tests skip; BB_REQUIRE_SANDBOX=1 makes them fail instead.
sandbox-image:
	docker pull $(IMAGE)

report:
	for run in results/*/; do echo "$$run"; python3 bench.py report "$$run"; done

clean:
	rm -rf $(HOME)/.cache/boundary-bench
