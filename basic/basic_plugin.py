#!python3
# https://nagios-plugins.org/doc/guidelines.html

# Import required libs for your plugin
# from x import y

# Return codes expected by Nagios
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Return message
message = {
    'status': OK,
    'summary': 'Example summary',
    'perfdata': 'label1=0;;;; '  # 'label'=value[UOM];[warn];[crit];[min];[max] 
}

# For multiple perdata, ensure to add space after each perfdata
# message['perfdata'] = 'label1=x;;;; '
# message['perfdata'] += 'label2=x;;;; '

def collect_data():
    ### some code here
    ### or calling external modules
    data = result_data
    return data

def check(data):
    """
    : param: example with data as int with a simple number to compare
    return: code status number (0, 1, 2 ,3) (See lines above)
    """
    ## Example check 
    pc = len(data)
    if pc >= 2:
        status = CRITICAL
        message['status'] = 'CRITICAL: '
    elif pc == 1:
        status = WARNING
        message['status'] = 'WARNING: '
    else:
        status = OK
        message['status'] = 'OK: '
    return status


# Check logic starts here
data = collect_data()
message['status'] += check(data)
# Add summary - you can also use more complex functions
message['summary'] = "SharepointHealth"
# Add perfdata - you can also use more complex functions
total = len(data)
message['perfdata'] = "alerts={};1;2;0; ".format(total)
# For multiple perdata, ensure to add space after each perfdata
# message['perfdata'] = 'label1=x;;;; '
# message['perfdata'] += 'label2=x;;;; '

# Print the message for nagios with perfdata
print("{summary}|{perfdata}".format(
    summary=message.get('summary'),
    perfdata=message.get('perfdata')
))

# Exit with status code
raise SystemExit(message['status'])

# Adding Argument parser, see:
# https://docs.python.org/3.5/library/argparse.html
