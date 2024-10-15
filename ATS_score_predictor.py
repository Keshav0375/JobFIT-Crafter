import json
import boto3
from dotenv import load_dotenv
import os
import logging
from botocore.exceptions import ClientError
from json import JSONDecodeError
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def ats_predictor(resume_text, job_description):
    logging.info("ATS")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
        "score": "",
        "keyword_insights": "",
        "missing_skills": [
            "",
            "",
            "",
            ""
        ],
        "resume_ranking": "",
        "flagging_issues": ""
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for ATS Scan of resumes based on job descriptions, in json format."
    prompt = f"Perform an ATS scan on the provided resume text: '{resume_text}' and job description: '{job_description}'." \
             f"Provide ATS score(in percentage), keyword insights, missing skills, resume ranking and flagging issues." \
             f"ATS score should be based on  keyword matches, skills, experience, and other factors. It tells recruiters how well the candidate fits the role. The higher the score, the more likely the candidate will be reviewed by a recruiter." \
             f"Keywrod insights should provide insights into how well the candidate’s experience aligns with specific parts of the job description" \
             f"Missing skills provide insights about which important qualifications or keywords are missing in a resume. " \
             f"Resume ranking tells which highest matching resumes presented first to recruiters and flagging issues are for ssues with resumes, such as lack of formatting compatibility, poor use of keywords, or missing elements that the job description emphasizes" \
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
        logging.info("ATS Done")
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