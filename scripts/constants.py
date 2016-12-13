# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Kubernetes branch to get the OpenAPI spec from.
KUBERNETES_BRANCH = "release-1.5"

# Spec version will be set in downloaded spec and all
# generated code will refer to it.
SPEC_VERSION = "v1.5.0-beta.3"

# client version for packaging and releasing. It can
# be different than SPEC_VERSION.
CLIENT_VERSION = "1.0.0-alpha.2"

# Name of the release package
PACKAGE_NAME = "kubernetes"