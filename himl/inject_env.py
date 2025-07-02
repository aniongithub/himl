# Copyright 2021 Adobe. All rights reserved.
# This file is licensed to you under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

from os import getenv
import re


class EnvVarInjector(object):
    """
    Resolve variables in the form:
    {{env(HOME)}}
    """

    def __init__(self):
        return

    def is_interpolation(self, value):
        return value.startswith('{{') and value.endswith('}}')

    def inject_env_var(self, line):
        """
        Check if the line contains environment variable interpolations and resolve them.
        """
        # Find all occurrences of {{env(...)}} using regex
        matches = re.findall(r"{{env\((.*?)\)}}", line)

        for env_var_name in matches:
            # Resolve the environment variable value
            env_value = getenv(env_var_name) or ""
            # Replace the interpolation with the resolved value
            line = line.replace(f"{{{{env({env_var_name})}}}}", env_value)

        return line

    def is_env_interpolation(self, value):
        return value.startswith('env(') and value.endswith(')')
