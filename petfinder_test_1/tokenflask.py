from flask import Flask, render_template, redirect, url_for, request
import requests





app = Flask(__name__)       # Get a flask object named app


@app.route('/tokenresponse', methods=['POST', 'GET']) 
def get_token():
        data = {
        'grant_type': 'client_credentials',
        'client_id': 'MbOpJgNCUBogNWLk8scTBvMqhJZrl5CJrrMcRsHKuQdWDotKsb',
        'client_secret': 'NEU5DXa7LfyL40OqleWPAKOrqpBZqVfzsPGxLSiP',
        }

        response = requests.post('https://api.petfinder.com/v2/oauth2/token', data=data)
    
        My_token = response.json()['access_token']
    
        return My_token     

  ########################################
    
if __name__ =='__main__':
    app.run(debug=True, port=8000)

    # eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJNYk9wSmdOQ1VCb2dOV0xrOHNjVEJ2TXFoSlpybDVDSnJyTWNSc0hLdVFkV0RvdEtzYiIsImp0aSI6IjA4NGI0N2M3OGRmMmIyYmI0ZDE1ZGFkMzEwOWY1ZTAzN2JhODQ0NjJmZDBmMjk3NWY2ZjZhZjljZDJjOGM2MWVkM2U0YzYyYWEzMDhiYmRjIiwiaWF0IjoxNjk4NjI5MDk0LCJuYmYiOjE2OTg2MjkwOTQsImV4cCI6MTY5ODYzMjY5NCwic3ViIjoiIiwic2NvcGVzIjpbXX0.y2N_3i7kXF-Kzh3V2_k-KHbVvazAvS3zkPGAmgczZS8BUAhiS-uLDcb0brlveQJ2Q3s5CGPgT-R6_MIEOjKDSsqXduuZxn94_RVbr2qrPZxvFqGz1p5Q30-4g2UMRpY_4t5YbEhJERdsghgjnhZffBzu7d1YX6IbIuvjSqpiv6QOfss0i1BoTdmUVv2d2hRBQU-nk8FsGX-ZsXzMv8aamAVLwYEgefM3mWABU2Zj98SqW3aQjVmt5EsPZ5rjXF3nhNRxeJXSGMCJOdkuvvven7t4k_wmGS_RvRKh0b3QDTo85DOPWmmI1OVd639a5LTfeeU2noIDqzVkAug0_vcZtw