.PHONY: all
all:
	uvicorn app.main:app --reload

.PHONY: i
i:
	pip install -r requirements.txt

YC_CR_URL=cr.yandex/crpa3cdlmumlpl95se5a

.PHONY: b
b:
	: "${RELEASE_TAG?Need to set RELEASE_TAG}"
	docker buildx build --platform linux/amd64 --tag $(YC_CR_URL)/tinkoffqna:$(RELEASE_TAG) --load . -f ./Dockerfile
	docker run --platform linux/amd64 --rm -p 8080:8080 --name tqna  $(YC_CR_URL)/tinkoffqna:$(RELEASE_TAG)
