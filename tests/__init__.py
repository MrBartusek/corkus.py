from vcr.config import VCR

def remove_headers():
    def before_record_response(response):
        response['headers'] = {}
        return response
    return before_record_response


vcr = VCR(
    cassette_library_dir = "tests/vcr_cassettes",
    path_transformer = VCR.ensure_suffix('.yaml'),
    before_record_response = remove_headers()
)
