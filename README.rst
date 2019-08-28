SSH manager
===========

SSH manager is a wrapper to the shell that enable features like:
- Fuzzy connection search
- Multiple commands on different connections
- Able to spawn commands to multiple commands 
    Example: sshmananer machines-{00.04} cd /logs/tomcat; grep 'ERROR' *

Testing
-------
Just run :code:`python3 -m unittest discover -s test/`
