# https://github.com/bimdata/docker-images/blob/main/Dockerfile.poetry
FROM docker-registry.bimdata.io/public/python-poetry:3.10 as builder-base


# https://github.com/bimdata/docker-images/blob/main/Dockerfile.django
FROM docker-registry.bimdata.io/public/python-django:3.10

# $PYSETUP_PATH contains all packages installed by poetry
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
