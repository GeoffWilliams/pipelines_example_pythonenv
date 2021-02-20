dist: env
	. env/bin/activate; \
	python setup.py sdist bdist_wheel

env:
	virtualenv env ; \
	. env/bin/activate; \
	pip install -r requirements.txt


publish: dist
	. env/bin/activate; \
	python setup.py bdist_wheel upload -r local

clean:
	rm -rf env
	rm -rf build
	rm -rf dist

.PHONY: clean dist