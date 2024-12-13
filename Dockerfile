FROM python:3.13.1-alpine AS base

# Install system dependencies
RUN apk add --no-cache tzdata
ENV TZ=${TZ:-Etc/UTC}

# Create user
ARG user=sub
ARG group=sub
ARG workdir="/app"
RUN addgroup --g 1000 ${group} && \
    adduser -u 1000 -G ${group} -h ${workdir} -D ${user}

# Setup data volume
ARG data_path="/data/"
RUN mkdir "${data_path}" && chown ${user}:${group} "${data_path}"
VOLUME [ "${data_path}" ]
ENV DATA_FILE="${data_path}sub.dat"

# Install dependencies
WORKDIR ${workdir}
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY sub/ sub/

# Run application
USER ${user}
ENTRYPOINT [ "python", "-m", "sub" ]
