FROM python:3.8.5

COPY . .

RUN pip install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com

EXPOSE 8888

CMD ["python", "api/main.py"]