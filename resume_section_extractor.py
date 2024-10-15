import json
import boto3
from dotenv import load_dotenv
import os
import logging
from botocore.exceptions import ClientError
from json import JSONDecodeError
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def extract_projects(text):
    logging.info("Projects Extraction")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "projects": {
              "names": [
                  "",
                  "",
                  ""
              ],
              "descriptions": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "dates": [
                  "",
                  "",
                  ""
              ],
              "technologies": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for extracting projects from resumes, in json format."
    prompt = f"Extract all projects mentioned in the resume text: '{text}'. " \
             f"For each project, extract the project names, descriptions, dates and technologies used. " \
             f"Format the extracted projects in four lists (names, descriptions as lists of lines, dates, and technologies as lists of tech)." \
             f"If any of these elements (names, descriptions, or dates) are missing for a project, return an empty string for that field. " \
             f"Ensure that each list has an entry for every project, even if some fields are empty. " \
             f"Strictly return the output in the format of a Python dictionary or JSON without any additional text or explanation. "

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Projects Found")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def extract_experience(text):
    logging.info("Experience Extraction")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "experiences": {
              "company_names": [
                  "",
                  "",
                  ""
              ],
              "positions": [
                  "",
                  "",
                  ""
              ],
              "descriptions": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "durations": [
                  "",
                  "",
                  ""
              ],
              "locations": [
                  "",
                  "",
                  ""
              ],
              "technologies": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "achievements": [
                  "",
                  "",
                  ""
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for extracting experiences from resumes, in json format."
    prompt = f"Extract all experiences mentioned in the resume text: '{text}'. " \
             f"For each experience, extract the project company names, positions, descriptions, durations, locations, technologies used and achievements. " \
             f"Format the extracted projects in seven lists (company_names, positions, descriptions as lists of lines, durations, locations, technologies as lists of tech and achievements)." \
             f"If any of these elements (company names, positions, descriptions, durations, locations, technologies used and achievements.) are missing for a experience, return an empty string for that field. " \
             f"Ensure that each list has an entry for every experience, even if some fields are empty. " \
             f"Strictly return the output in the format of a Python dictionary or JSON without any additional text or explanation. "

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Experience Found")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def extract_skills(text):
    logging.info("Skills Extraction")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "skills": {
              "technical_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "tools/frameworks": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "soft_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "analytical_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "spoken_languages": [
                  "",
                  "",
                  ""
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for extracting skills from resumes, in json format."
    prompt = f"Extract all skills mentioned in the resume text: '{text}'. " \
             f"Divide and put the extracted skills in five lists (technical skills, tools/frameworks, soft skills, analytical skills and spoken languages)." \
             f"If any category has no skills listed, return an empty list for that category. " \
             f"Strictly return the output in the format of a Python dictionary or JSON without any additional text or explanation. "

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Skills Found")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def extract_education(text):
    logging.info("Education Extraction")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "educations": {
              "institutions": [
                  "",
                  "",
                  ""
              ],
              "programs": [
                  "",
                  "",
                  ""
              ],
              "durations": [
                  "",
                  "",
                  ""
              ],
              "marks": [
                  "",
                  "",
                  ""
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for extracting education from resumes, in json format."
    prompt = f"Extract all educations mentioned in the resume text: '{text}'. " \
             f"For each education, extract the institution, program, duration and marks. " \
             f"Format the extracted education in four lists (institutions, programs, durations and marks)." \
             f"If any of these elements (institutions, programs, durations and marks) are missing for a project, return an empty string for that field. " \
             f"Ensure that each list has an entry for every education, even if some fields are empty. " \
             f"Strictly return the output in the format of a Python dictionary or JSON without any additional text or explanation. "

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Education Found")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def extract_contact_info(text):
    logging.info("Contact Info Extraction")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
        "name": "",
        "contact_number": "",
        "email": "",
        "github_url": "",
        "linkedin_url": ""
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for extracting contact info from resumes, in json format."
    prompt = f"Extract all contact information mentioned in the resume text: '{text}'. " \
             f"Extract name, contact number, email, github url and linkedin url. " \
             f"If any of these elements (name, contact_number, email, github_url and linkedin_url) are missing, return an empty string for that field. " \
             f"Strictly return the output in the format of a Python dictionary or JSON without any additional text or explanation. "

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Contact Info Found")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_