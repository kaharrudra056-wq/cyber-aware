"""Run this once to populate the database with initial data."""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from models import db
from models.user import User
from models.quiz import Topic, Question

app = create_app()

TOPICS = [
    {
        'title': 'Password Security',
        'slug': 'password-security',
        'icon': '🔑',
        'order': 1,
        'description': 'Learn how to create and manage strong passwords.',
        'content': '''<h4>Why Passwords Matter</h4>
<p>Passwords are your first line of defense against unauthorized access. A weak password can be cracked in seconds using brute-force tools.</p>
<h4>Rules for a Strong Password</h4>
<ul>
  <li>At least <strong>12 characters</strong> long</li>
  <li>Mix of <strong>uppercase, lowercase, numbers, and symbols</strong></li>
  <li>Avoid dictionary words, names, or birthdates</li>
  <li>Never reuse passwords across sites</li>
  <li>Use a <strong>password manager</strong> (Bitwarden, 1Password)</li>
</ul>
<h4>Examples</h4>
<table class="table table-bordered">
  <thead><tr><th>Weak ❌</th><th>Strong ✅</th></tr></thead>
  <tbody>
    <tr><td>password123</td><td>Tr@7#kL92!xQ</td></tr>
    <tr><td>john1990</td><td>J0hn$@19-90!</td></tr>
    <tr><td>abc123</td><td>@Bc!23#XyZ99</td></tr>
  </tbody>
</table>
<h4>Two-Factor Authentication (2FA)</h4>
<p>Even with a strong password, enable 2FA wherever possible. This adds a second layer of verification.</p>'''
    },
    {
        'title': 'Phishing Attacks',
        'slug': 'phishing',
        'icon': '🎣',
        'order': 2,
        'description': 'Identify and avoid phishing emails and websites.',
        'content': '''<h4>What is Phishing?</h4>
<p>Phishing is a cyberattack where criminals impersonate trusted organizations to steal your credentials, financial info, or install malware.</p>
<h4>Common Phishing Tactics</h4>
<ul>
  <li><strong>Email phishing:</strong> Fake emails from banks, Netflix, etc.</li>
  <li><strong>Smishing:</strong> Phishing via SMS</li>
  <li><strong>Vishing:</strong> Phone call phishing</li>
  <li><strong>Spear phishing:</strong> Targeted attacks using your personal info</li>
</ul>
<h4>Red Flags 🚩</h4>
<ul>
  <li>Urgent language: "Your account will be closed in 24 hours!"</li>
  <li>Suspicious sender domain (e.g., support@paypa1.com)</li>
  <li>Unexpected attachments</li>
  <li>Generic greeting: "Dear Customer"</li>
  <li>Links that don\'t match the displayed text</li>
</ul>
<h4>How to Stay Safe</h4>
<ul>
  <li>Never click links in unsolicited emails — go directly to the website</li>
  <li>Check the actual email address, not just the display name</li>
  <li>Use email filters and anti-phishing browser extensions</li>
  <li>Report phishing to your IT team or email provider</li>
</ul>'''
    },
    {
        'title': 'Malware Protection',
        'slug': 'malware',
        'icon': '🦠',
        'order': 3,
        'description': 'Understand malware types and how to protect yourself.',
        'content': '''<h4>What is Malware?</h4>
<p>Malware (malicious software) is any software designed to harm your computer, steal data, or gain unauthorized access.</p>
<h4>Types of Malware</h4>
<ul>
  <li><strong>Virus:</strong> Self-replicating code that attaches to files</li>
  <li><strong>Ransomware:</strong> Encrypts your files and demands payment</li>
  <li><strong>Spyware:</strong> Secretly monitors your activity</li>
  <li><strong>Trojans:</strong> Disguised as legitimate software</li>
  <li><strong>Adware:</strong> Displays unwanted advertisements</li>
  <li><strong>Worms:</strong> Spread across networks without user action</li>
</ul>
<h4>Prevention Tips</h4>
<ul>
  <li>Keep your OS and software <strong>updated</strong></li>
  <li>Install a reputable <strong>antivirus</strong></li>
  <li>Download software only from <strong>official sources</strong></li>
  <li>Avoid clicking on <strong>pop-up ads</strong></li>
  <li>Regularly <strong>backup your data</strong></li>
</ul>'''
    },
    {
        'title': 'Social Engineering',
        'slug': 'social-engineering',
        'icon': '👤',
        'order': 4,
        'description': 'Recognize social engineering and manipulation tactics.',
        'content': '''<h4>What is Social Engineering?</h4>
<p>Social engineering exploits human psychology rather than technical vulnerabilities to gain access to systems or information.</p>
<h4>Common Techniques</h4>
<ul>
  <li><strong>Pretexting:</strong> Creating a fabricated scenario to extract info</li>
  <li><strong>Baiting:</strong> Offering something enticing (free USB drive with malware)</li>
  <li><strong>Quid pro quo:</strong> Offering a service in exchange for information</li>
  <li><strong>Tailgating:</strong> Physically following an authorized person into a secure area</li>
</ul>
<h4>Protection</h4>
<ul>
  <li>Verify identities before sharing information</li>
  <li>Be skeptical of unsolicited requests</li>
  <li>Follow your organization\'s security policies</li>
  <li>Train yourself to recognize manipulation tactics</li>
</ul>'''
    },
    {
        'title': 'Safe Browsing',
        'slug': 'safe-browsing',
        'icon': '🌐',
        'order': 5,
        'description': 'Browse the internet safely and securely.',
        'content': '''<h4>Safe Browsing Practices</h4>
<ul>
  <li>Always check for <strong>HTTPS</strong> (padlock icon) before entering data</li>
  <li>Use a <strong>VPN</strong> on public networks</li>
  <li>Keep your <strong>browser updated</strong></li>
  <li>Use <strong>privacy-focused extensions</strong> (uBlock Origin, Privacy Badger)</li>
  <li>Avoid <strong>piracy sites</strong> — they often distribute malware</li>
  <li>Clear cookies and cache regularly</li>
</ul>
<h4>Recognizing Fake Websites</h4>
<ul>
  <li>Check for slight domain misspellings (amaz0n.com)</li>
  <li>Poor design, grammar mistakes</li>
  <li>No contact information or privacy policy</li>
  <li>Pressure to act quickly</li>
</ul>'''
    },
    {
        'title': 'Two-Factor Authentication',
        'slug': '2fa',
        'icon': '🔐',
        'order': 6,
        'description': 'Enable 2FA to add an extra layer of security.',
        'content': '''<h4>What is 2FA?</h4>
<p>Two-Factor Authentication (2FA) requires two forms of verification before granting access — something you <em>know</em> (password) and something you <em>have</em> (phone/token).</p>
<h4>Types of 2FA</h4>
<ul>
  <li><strong>SMS OTP:</strong> Code sent to your phone (least secure)</li>
  <li><strong>Authenticator App:</strong> Google Authenticator, Authy (recommended)</li>
  <li><strong>Hardware key:</strong> YubiKey (most secure)</li>
  <li><strong>Biometrics:</strong> Fingerprint, face recognition</li>
</ul>
<h4>Enable 2FA everywhere</h4>
<p>Always enable 2FA on: Email, Banking, Social Media, Cloud Storage, and any service storing sensitive data.</p>'''
    },
    {
        'title': 'Public Wi-Fi Safety',
        'slug': 'public-wifi',
        'icon': '📶',
        'order': 7,
        'description': 'Stay safe on public Wi-Fi networks.',
        'content': '''<h4>Risks of Public Wi-Fi</h4>
<ul>
  <li><strong>Man-in-the-Middle attacks:</strong> Attackers intercept your traffic</li>
  <li><strong>Evil twin attacks:</strong> Fake hotspot mimicking a real one</li>
  <li><strong>Packet sniffing:</strong> Capturing unencrypted data</li>
</ul>
<h4>Stay Safe</h4>
<ul>
  <li>Use a <strong>VPN</strong> always on public Wi-Fi</li>
  <li>Avoid accessing banking or sensitive accounts</li>
  <li>Turn off <strong>auto-connect</strong> to Wi-Fi</li>
  <li>Use <strong>HTTPS-only</strong> websites</li>
  <li>Forget public networks after use</li>
</ul>'''
    },
    {
        'title': 'Mobile Security',
        'slug': 'mobile-security',
        'icon': '📱',
        'order': 8,
        'description': 'Keep your smartphone and apps secure.',
        'content': '''<h4>Mobile Security Tips</h4>
<ul>
  <li>Use a strong <strong>PIN/biometric lock</strong></li>
  <li>Only install apps from <strong>official stores</strong> (Play Store, App Store)</li>
  <li>Review app <strong>permissions</strong> before granting</li>
  <li>Keep your OS and apps <strong>updated</strong></li>
  <li>Enable <strong>remote wipe</strong> in case of theft</li>
  <li>Avoid rooting/jailbreaking your device</li>
  <li>Use encrypted messaging apps (Signal)</li>
</ul>
<h4>Recognizing Malicious Apps</h4>
<ul>
  <li>Requests unnecessary permissions (flashlight asking for contacts)</li>
  <li>Poor reviews mentioning battery drain or data usage spikes</li>
  <li>Unknown developers with few downloads</li>
</ul>'''
    },
]

QUESTIONS = [
    # Password Security
    {'topic_slug': 'password-security', 'question_text': 'Which of the following is the strongest password?', 'option_a': '123456', 'option_b': 'password', 'option_c': 'Dh@7#kL92!x', 'option_d': 'john1990', 'correct_answer': 'C', 'explanation': 'Dh@7#kL92!x uses uppercase, lowercase, numbers and symbols making it very strong.'},
    {'topic_slug': 'password-security', 'question_text': 'What is the minimum recommended password length?', 'option_a': '4 characters', 'option_b': '6 characters', 'option_c': '8 characters', 'option_d': '12 characters', 'correct_answer': 'D', 'explanation': 'Security experts recommend at least 12 characters for a strong password.'},
    {'topic_slug': 'password-security', 'question_text': 'Which is the safest way to store passwords?', 'option_a': 'Write them in a notebook', 'option_b': 'Use a password manager', 'option_c': 'Use the same password everywhere', 'option_d': 'Save in a text file', 'correct_answer': 'B', 'explanation': 'Password managers securely encrypt and store all your passwords.'},
    {'topic_slug': 'password-security', 'question_text': 'What does 2FA stand for?', 'option_a': 'Two Files Access', 'option_b': 'Two-Factor Authentication', 'option_c': 'Two Firewall Authenticity', 'option_d': 'Two Fast Authorizations', 'correct_answer': 'B', 'explanation': '2FA = Two-Factor Authentication — an extra layer of account security.'},
    # Phishing
    {'topic_slug': 'phishing', 'question_text': 'Which is a red flag that an email might be a phishing attempt?', 'option_a': 'It comes from a known friend', 'option_b': 'It has your full name in the greeting', 'option_c': 'It creates urgency: "Your account expires in 24 hours!"', 'option_d': 'It has no attachments', 'correct_answer': 'C', 'explanation': 'Urgency is a classic phishing tactic designed to make you act without thinking.'},
    {'topic_slug': 'phishing', 'question_text': 'What should you do if you receive a suspicious email from your bank?', 'option_a': 'Click the link and enter your details', 'option_b': 'Forward it to all your contacts', 'option_c': 'Delete it and go directly to your bank website', 'option_d': 'Reply asking for more information', 'correct_answer': 'C', 'explanation': 'Never click links in suspicious emails. Go directly to the official website.'},
    {'topic_slug': 'phishing', 'question_text': 'What is spear phishing?', 'option_a': 'Phishing using a fishing rod', 'option_b': 'A targeted phishing attack using personal information', 'option_c': 'Phishing via SMS', 'option_d': 'Phishing on social media', 'correct_answer': 'B', 'explanation': 'Spear phishing is a targeted attack that uses personal details to seem more legitimate.'},
    # Malware
    {'topic_slug': 'malware', 'question_text': 'What type of malware encrypts your files and demands payment?', 'option_a': 'Spyware', 'option_b': 'Adware', 'option_c': 'Ransomware', 'option_d': 'Worm', 'correct_answer': 'C', 'explanation': 'Ransomware encrypts files and demands a ransom payment, usually in cryptocurrency.'},
    {'topic_slug': 'malware', 'question_text': 'Which action best prevents malware infection?', 'option_a': 'Using only one browser', 'option_b': 'Keeping software updated and using antivirus', 'option_c': 'Downloading from any website', 'option_d': 'Disabling your firewall', 'correct_answer': 'B', 'explanation': 'Regular updates patch security vulnerabilities and antivirus detects known malware.'},
    # Safe Browsing
    {'topic_slug': 'safe-browsing', 'question_text': 'What does HTTPS indicate about a website?', 'option_a': 'It is a government website', 'option_b': 'The connection is encrypted', 'option_c': 'The website is safe from all threats', 'option_d': 'It requires a login', 'correct_answer': 'B', 'explanation': 'HTTPS encrypts data between your browser and the server, protecting it from interception.'},
    {'topic_slug': 'safe-browsing', 'question_text': 'What is the best way to identify a fake website?', 'option_a': 'Check if it has colorful design', 'option_b': 'Check for domain misspellings and missing HTTPS', 'option_c': 'See if it loads fast', 'option_d': 'Check if it has many images', 'correct_answer': 'B', 'explanation': 'Fake websites often have slight domain misspellings and may lack HTTPS.'},
    # 2FA
    {'topic_slug': '2fa', 'question_text': 'Which form of 2FA is considered most secure?', 'option_a': 'SMS OTP', 'option_b': 'Email OTP', 'option_c': 'Authenticator App', 'option_d': 'Hardware Security Key', 'correct_answer': 'D', 'explanation': 'Hardware keys like YubiKey are the most secure 2FA method as they cannot be phished remotely.'},
    # Public Wi-Fi
    {'topic_slug': 'public-wifi', 'question_text': 'What is an "evil twin" attack?', 'option_a': 'A virus that creates duplicate files', 'option_b': 'A fake Wi-Fi hotspot mimicking a legitimate one', 'option_c': 'Two identical phishing emails', 'option_d': 'A malware that clones your identity', 'correct_answer': 'B', 'explanation': 'An evil twin is a rogue Wi-Fi access point that appears identical to a legitimate one to intercept traffic.'},
    {'topic_slug': 'public-wifi', 'question_text': 'What should you use when connecting to public Wi-Fi?', 'option_a': 'A proxy server', 'option_b': 'A VPN', 'option_c': 'Incognito mode', 'option_d': 'A different browser', 'correct_answer': 'B', 'explanation': 'A VPN encrypts your internet traffic, protecting it even on unsecured public networks.'},
    # Mobile Security
    {'topic_slug': 'mobile-security', 'question_text': 'What is a sign that a mobile app might be malicious?', 'option_a': 'It has a colorful icon', 'option_b': 'It requests unnecessary permissions', 'option_c': 'It is free to download', 'option_d': 'It is listed in the app store', 'correct_answer': 'B', 'explanation': 'Malicious apps often request permissions unrelated to their function to steal data.'},
    # Social Engineering
    {'topic_slug': 'social-engineering', 'question_text': 'What is "pretexting" in social engineering?', 'option_a': 'Sending a fake text message', 'option_b': 'Creating a fabricated scenario to extract information', 'option_c': 'Pretending to be a technical expert online', 'option_d': 'Accessing a system before authentication', 'correct_answer': 'B', 'explanation': 'Pretexting involves creating a believable story to manipulate someone into revealing information.'},
]

def seed():
    with app.app_context():
        # Create admin user
        if not User.query.filter_by(email='admin@cybersec.com').first():
            admin = User(username='admin', email='admin@cybersec.com', is_admin=True)
            admin.set_password('Admin@1234')
            db.session.add(admin)
            print('✅ Admin user created: admin@cybersec.com / Admin@1234')

        # Create topics
        topic_map = {}
        for t in TOPICS:
            existing = Topic.query.filter_by(slug=t['slug']).first()
            if not existing:
                topic = Topic(**t)
                db.session.add(topic)
                db.session.flush()
                topic_map[t['slug']] = topic
                print(f'✅ Topic: {t["title"]}')
            else:
                topic_map[t['slug']] = existing

        db.session.commit()

        # Create questions
        for q in QUESTIONS:
            slug = q.pop('topic_slug')
            topic = topic_map.get(slug)
            if topic and not Question.query.filter_by(question_text=q['question_text']).first():
                question = Question(topic_id=topic.id, **q)
                db.session.add(question)
                print(f'✅ Question added for {slug}')
            q['topic_slug'] = slug  # restore

        db.session.commit()
        print('\n🎉 Database seeded successfully!')
        print('Admin: admin@cybersec.com | Password: Admin@1234')

if __name__ == '__main__':
    seed()
