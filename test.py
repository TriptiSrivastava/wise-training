import math #imports math

import math #imports math
import math #imports math
import math #imports math
import os as os_orig
import utils
import sys
from django.http import HttpResponse
from django.shortcuts import render_to_response
from attendance.models import *
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate


