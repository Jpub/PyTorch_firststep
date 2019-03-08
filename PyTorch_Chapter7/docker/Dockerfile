FROM nvidia/cuda:9.0-base

# Miniconda를 설치하기 위한 최소 패키지 설치
RUN set -ex \
    && deps=' \
        bzip2 \
        ca-certificates \
        curl \
        libgomp1 \
        libgfortran3 \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $deps \
    && rm -rf /var/lib/apt/lists/*

ENV PKG_URL https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
ENV INSTALLER miniconda.sh

# miniconda 설치
RUN set -ex \
    && curl -kfSL $PKG_URL -o $INSTALLER \
    && chmod 755 $INSTALLER \
    && ./$INSTALLER -b -p /opt/conda3 \
    && rm $INSTALLER

# miniconda룰  PATH에 추가
ENV PATH /opt/conda3/bin:$PATH

# PyTorch v1.0 설치
ENV PYTORCH_VERSION 1.0

RUN set -ex \
    && pkgs=" \
        pytorch=${PYTORCH_VERSION} \
        torchvision \
    " \
    && conda install -y ${pkgs} -c pytorch \
    && conda clean -i -l -t -y
