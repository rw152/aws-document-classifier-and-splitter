import requests


def split_s3_pdf(dns_name, input_pdf_uri, bucket_name, endpoint_arn):
    if dns_name.endswith("/"):
        path = "s3_file"
    else:
        path = "/s3_file"

    queries = f"?bucket_name={bucket_name}&endpoint_arn={endpoint_arn}&input_pdf_uri={input_pdf_uri}"
    url = dns_name + path + queries
    response = requests.post(url)
    print(response.text)


if __name__ == "__main__":
    dns_name = "http://docsp-loadb-1n8juvn1kj8-627401827.us-east-1.elb.amazonaws.com/"
    bucket_name = "logix-docsplitter-uploads"
    endpoint_arn = "arn:aws:comprehend:us-east-1:486871406290:document-classifier-endpoint/Classifier-20221030143002"

    # Z:\GitHub\PLANELOGIX\aws-document-classifier-and-splitter\workflow3_local\01_Aircraft_Maintenance_Log_Binder.pdf
    input_pdf_path = "s3://logix-docsplitter-uploads/N51PV/01_Aircraft_Maintenance_Log_Binder.pdf"

    split_s3_pdf(dns_name, input_pdf_path, bucket_name, endpoint_arn)
