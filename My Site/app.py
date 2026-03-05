from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # এখানে তোমার নাম এবং বর্ণনা পরিবর্তন করো
    my_name = "তোমার নাম" 
    
    html_content = f"""
    <html>
        <head>
            <title>{my_name} এর ওয়েবসাইট</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f0f2f5; padding-top: 50px; }}
                .container {{ background: white; padding: 40px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
                h1 {{ color: #007bff; }}
                p {{ color: #555; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>হ্যালো, আমি {my_name}!</h1>
                <p>এটি পাইথন (Flask) দিয়ে তৈরি আমার ছোট একটি ওয়েবসাইট।</p>
                <hr>
                <p>নতুন কিছু শেখার যাত্রা শুরু হোক!</p>
            </div>
        </body>
    </html>
    """
    return html_content

if __name__ == '__main__':
    app.run(debug=True)
