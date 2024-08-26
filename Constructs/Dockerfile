# Start from lambda Python3.8 image
FROM public.ecr.aws/lambda/python:3.8

# Copy the lambda code, together with its requirements
COPY lambda/requirements.txt ${LAMBDA_TASK_ROOT}
COPY lambda/lambda_code.py ${LAMBDA_TASK_ROOT}

# Install postgresql-devel in your image
RUN yum install -y gcc postgresql-devel

# install the requirements for the Lambda code
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Command can be overwritten by providing a different command in the template directly.
CMD ["lambda_code.handler"]