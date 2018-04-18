FROM python:3-onbuild
EXPOSE 8000
CMD ["python", "./http_server.py"]
