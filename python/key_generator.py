"""
-------------------------------------------------------------------------------
key_generator.py

Create Date:    2023-02-21
Author:         Stefan Dombek <dombek@uni-leipzig.de>
Description:    This script creates a key to encrypt the login credentials and
                encrypt the credentials.
-------------------------------------------------------------------------------
Copyright (C) 2018-2023 The Open Library Foundation

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
-------------------------------------------------------------------------------
"""
###############################################################################
#                                                                             #
# Load modules                                                                #
#                                                                             #
###############################################################################
from cryptography.fernet import Fernet

###############################################################################
#                                                                             #
# Generate key for encryption                                                 #
#                                                                             #
###############################################################################
key = Fernet.generate_key()

config_key = open('config.key', 'wb')
config_key.write(key)

###############################################################################
#                                                                             #
# Encrypt credentials                                                         #
#                                                                             #
###############################################################################

# load key
f = Fernet(key)

# open original file with login credentials
orginal_file = open('credentials.csv', 'rb')
content_original_file = orginal_file.read()

# encrypt the file
encrypted = f.encrypt(content_original_file)
encrypted_file = open('enc_credentials.csv', 'wb')
encrypted_file.write(encrypted)
