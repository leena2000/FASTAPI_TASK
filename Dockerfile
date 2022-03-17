FROM python

# set working directory
WORKDIR /app

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

CMD 'sh'
