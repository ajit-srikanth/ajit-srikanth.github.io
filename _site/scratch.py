import re

with open('_layouts/default.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the pageBg tinted
content = re.sub(r"id: 'robotics',\s*name: 'Robotics',([\s\S]*?)courtSize: '40px 40px'", r"id: 'robotics',\n        name: 'Robotics',\1courtSize: '40px 40px',\n        pageBg: 'rgba(235, 240, 255, 0.92)'", content)

# Tennis
tennis_lines = "linear-gradient(90deg, transparent 10%, rgba(255,255,255,0.6) 10%, rgba(255,255,255,0.6) 10.5%, transparent 10.5%, transparent 89.5%, rgba(255,255,255,0.6) 89.5%, rgba(255,255,255,0.6) 90%, transparent 90%), linear-gradient(transparent 50%, rgba(255,255,255,0.6) 50%, rgba(255,255,255,0.6) 50.5%, transparent 50.5%)"
content = re.sub(r"id: 'tennis',\s*name: 'Tennis',([\s\S]*?)courtBase: '#1a432b',\s*courtLines: '[^']*',\s*courtSize: '100px 100px'", f"id: 'tennis',\n        name: 'Tennis',\1courtBase: '#255e3c',\n        courtLines: '{tennis_lines}',\n        courtSize: '100% 100%',\n        pageBg: 'rgba(235, 250, 240, 0.92)'", content)

# Basketball
bb_lines = "linear-gradient(90deg, transparent 35%, rgba(255,255,255,0.6) 35%, rgba(255,255,255,0.6) 35.5%, transparent 35.5%, transparent 64.5%, rgba(255,255,255,0.6) 64.5%, rgba(255,255,255,0.6) 65%, transparent 65%), linear-gradient(rgba(255,255,255,0.6) 2px, transparent 2px), radial-gradient(circle at 50% 100px, transparent 150px, rgba(255,255,255,0.6) 150px, rgba(255,255,255,0.6) 152px, transparent 152px)"
content = re.sub(r"id: 'basketball',\s*name: 'Basketball',([\s\S]*?)courtBase: '#7a3100',\s*courtLines: '[^']*',\s*courtSize: '150px 150px'", f"id: 'basketball',\n        name: 'Basketball',\1courtBase: '#d98741',\n        courtLines: '{bb_lines}',\n        courtSize: '100% 100%',\n        pageBg: 'rgba(255, 240, 230, 0.92)'", content)

# Football
content = re.sub(r"id: 'football',\s*name: 'Football',([\s\S]*?)courtSize: '100% 100%'", r"id: 'football',\n        name: 'Football',\1courtSize: '100% 100%',\n        pageBg: 'rgba(235, 250, 235, 0.92)'", content)

# Swimming
content = re.sub(r"id: 'swimming',\s*name: 'Swimming',([\s\S]*?)courtSize: '120px 100%'", r"id: 'swimming',\n        name: 'Swimming',\1courtSize: '120px 100%',\n        pageBg: 'rgba(230, 245, 255, 0.92)'", content)

# Cricket
content = re.sub(r"id: 'cricket',\s*name: 'Cricket',([\s\S]*?)courtSize: '400px 400px'", r"id: 'cricket',\n        name: 'Cricket',\1courtSize: '400px 400px',\n        pageBg: 'rgba(250, 240, 230, 0.92)'", content)

# Table Tennis
content = re.sub(r"id: 'table-tennis',\s*name: 'Table Tennis',([\s\S]*?)courtSize: '50vw 50vh'", r"id: 'table-tennis',\n        name: 'Table Tennis',\1courtSize: '50vw 50vh',\n        pageBg: 'rgba(230, 235, 255, 0.92)'", content)

# Volleyball
content = re.sub(r"id: 'volleyball',\s*name: 'Volleyball',([\s\S]*?)courtSize: '50% 100%'", r"id: 'volleyball',\n        name: 'Volleyball',\1courtSize: '50% 100%',\n        pageBg: 'rgba(230, 250, 255, 0.92)'", content)

# Badminton
content = re.sub(r"id: 'badminton',\s*name: 'Badminton',([\s\S]*?)courtSize: '150px 80px'", r"id: 'badminton',\n        name: 'Badminton',\1courtSize: '150px 80px',\n        pageBg: 'rgba(230, 250, 245, 0.92)'", content)

with open('_layouts/default.html', 'w', encoding='utf-8') as f:
    f.write(content)
