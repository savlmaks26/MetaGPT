# Use a base image with Python3.9 and Nodejs20 slim version
FROM nikolaik/python-nodejs:python3.9-nodejs20-slim

# Install Debian software needed by MetaGPT
RUN apt update &&\
    apt install -y git chromium fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 --no-install-recommends &&\
    apt clean

# Install Mermaid CLI globally
ENV CHROME_BIN="/usr/bin/chromium" \
    PUPPETEER_CONFIG="/project/home/savlmaks26/workspace/config/config.yaml"\
    PUPPETEER_SKIP_CHROMIUM_DOWNLOAD="true"
RUN npm install -g @mermaid-js/mermaid-cli &&\
    npm cache clean --force

# Install Python dependencies and install MetaGPT
COPY . /project/home/savlmaks26/workspace/metagpt
RUN cd /project/home/savlmaks26/workspace/metagpt &&\
    mkdir workspace
#RUN cd /project/home/savlmaks26/workspace/ && python setup.py install

WORKDIR /project/home/savlmaks26/workspace/metagpt

# Running with an infinite loop using the tail command
CMD ["sh", "-c", "tail -f /dev/null"]
