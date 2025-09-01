from flask import Flask, render_template, request, jsonify
import sys
import os

# Add src directory to path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from hackclub_ai import generate_better_prompt, ask_hackclub

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/optimize-prompt', methods=['POST'])
def optimize_prompt():
    try:
        data = request.get_json()
        intent = data.get('intent', '')
        user_text = data.get('user_text', '')
        
        if not intent or not user_text:
            return jsonify({'error': 'Both intent and user_text are required'}), 400
        
        optimized_prompt = generate_better_prompt(intent, user_text)
        return jsonify({'optimized_prompt': optimized_prompt})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/complete', methods=['POST'])
def complete():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        model = data.get('model', 'qwen/qwen3-32b')
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        completion = ask_hackclub(prompt, model)
        return jsonify({'completion': completion})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
