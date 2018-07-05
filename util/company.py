# -*- coding: utf-8 -*-

# =====================================================================
# write : moto
# latest update : 18.05.23.
#
# usage : python parsing_filaV1.py
# =====================================================================


import datetime, sys, json, subprocess, time, urllib2
from os import popen, path
from os.path import expanduser
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen, URLError, HTTPError
from sys import platform
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



reload(sys)
sys.setdefaultencoding('utf-8')


aaa = """
<tbody id="grdCompCmp_body_tbody"><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_0_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="0" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_0_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="1" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01160</nobr></td><td id="grdCompCmp_cell_0_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="2" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국성장금융투자운용</nobr></td><td id="grdCompCmp_cell_0_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="3" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국성장금융투자운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_1_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="4" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_1_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="5" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01140</nobr></td><td id="grdCompCmp_cell_1_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="6" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국자산에셋운용</nobr></td><td id="grdCompCmp_cell_1_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="7" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국자산에셋운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_2_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="8" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_2_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="9" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01044</nobr></td><td id="grdCompCmp_cell_2_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="10" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국투자밸류자산운용</nobr></td><td id="grdCompCmp_cell_2_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="11" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국투자밸류자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_3_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="12" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_3_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="13" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01001</nobr></td><td id="grdCompCmp_cell_3_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="14" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국투자신탁운용</nobr></td><td id="grdCompCmp_cell_3_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="15" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국투자신탁운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_4_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="16" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_4_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="17" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01179</nobr></td><td id="grdCompCmp_cell_4_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="18" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한앤파트너스자산운용</nobr></td><td id="grdCompCmp_cell_4_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="19" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한앤파트너스자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_5_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="20" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_5_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="21" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01199</nobr></td><td id="grdCompCmp_cell_5_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="22" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한일퍼스트자산운용</nobr></td><td id="grdCompCmp_cell_5_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="23" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한일퍼스트자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_6_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="24" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_6_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="25" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01021</nobr></td><td id="grdCompCmp_cell_6_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="26" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한화자산운용</nobr></td><td id="grdCompCmp_cell_6_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="27" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한화자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_7_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="28" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_7_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="29" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01214</nobr></td><td id="grdCompCmp_cell_7_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="30" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>헤이스팅스자산운용</nobr></td><td id="grdCompCmp_cell_7_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="31" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>헤이스팅스자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_8_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="32" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_8_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="33" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01047</nobr></td><td id="grdCompCmp_cell_8_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="34" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대인베스트먼트자산운용</nobr></td><td id="grdCompCmp_cell_8_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="35" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대인베스트먼트자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_9_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="36" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_9_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="37" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01082</nobr></td><td id="grdCompCmp_cell_9_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="38" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대자산운용</nobr></td><td id="grdCompCmp_cell_9_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="39" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_10_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="40" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_10_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="41" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01175</nobr></td><td id="grdCompCmp_cell_10_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="42" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>휴먼자산운용</nobr></td><td id="grdCompCmp_cell_10_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="43" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>휴먼자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(255, 255, 255);" role="row" trindex="0" class="grid_body_row"><td id="grdCompCmp_cell_11_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_ focusedTr" style="text-align: center; background-color: rgb(243, 249, 246);" col_id="vGridChkBox" tdindex="44" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
};background-color:#F3F9F6" or_bgcolor="rgb(243, 249, 246)"><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_11_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_ focusedTr" style="text-align: left; background-color: rgb(243, 249, 246);" col_id="companyCd" tdindex="45" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
};background-color:#F3F9F6" or_bgcolor="rgb(243, 249, 246)"><nobr>A01032</nobr></td><td id="grdCompCmp_cell_11_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_ focusedTr" style="text-align: left; background-color: rgb(243, 249, 246);" col_id="koreanNm" tdindex="46" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
};background-color:#F3F9F6" or_bgcolor="rgb(243, 249, 246)"><nobr>흥국자산운용</nobr></td><td id="grdCompCmp_cell_11_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_ focusedTr" style="text-align: left; background-color: rgb(243, 249, 246);" col_id="uCpnyNm" tdindex="47" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
};background-color:#F3F9F6" or_bgcolor="rgb(243, 249, 246)" tabindex="0"><nobr>흥국자산운용</nobr></td></tr><tr id="row8" style="background-color: rgb(241, 247, 254); display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_12_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="48" or_wd="32" or_bgcolor="" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}"><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_12_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="49" or_wd="100" or_bgcolor="" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}"><nobr>A01021</nobr></td><td id="grdCompCmp_cell_12_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="50" or_wd="220" or_bgcolor="" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}"><nobr>한화자산운용</nobr></td><td id="grdCompCmp_cell_12_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="51" or_wd="220" or_bgcolor="" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}"><nobr>현대자산운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_13_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="52" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_13_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="53" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01214</nobr></td><td id="grdCompCmp_cell_13_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="54" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>헤이스팅스자산운용</nobr></td><td id="grdCompCmp_cell_13_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="55" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>휴먼자산운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_14_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="56" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_14_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="57" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01047</nobr></td><td id="grdCompCmp_cell_14_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="58" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대인베스트먼트자산운용</nobr></td><td id="grdCompCmp_cell_14_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="59" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>흥국자산운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_15_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="60" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_15_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="61" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01082</nobr></td><td id="grdCompCmp_cell_15_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="62" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>현대자산운용</nobr></td><td id="grdCompCmp_cell_15_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="63" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한국투자신탁운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_16_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="64" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_16_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="65" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01175</nobr></td><td id="grdCompCmp_cell_16_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="66" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>휴먼자산운용</nobr></td><td id="grdCompCmp_cell_16_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="67" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한앤파트너스자산운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_17_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="68" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_17_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="69" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>A01032</nobr></td><td id="grdCompCmp_cell_17_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="70" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>흥국자산운용</nobr></td><td id="grdCompCmp_cell_17_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="71" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한일퍼스트자산운용</nobr></td></tr><tr id="row8" style="display: none;" role="row" trindex="0" class="grid_body_row w2grid_hidedRow"><td id="grdCompCmp_cell_18_0" readonly="false" inputtype="checkbox" colindex="0" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_0_" style="text-align: center;" col_id="vGridChkBox" tdindex="72" or_wd="32" style_bak="text-align:center;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><input style="border-width:0px;" type="checkbox" tabindex="-1"></td><td id="grdCompCmp_cell_18_1" readonly="true" inputtype="text" textalign="left" colindex="1" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_1_" style="text-align: left;" col_id="companyCd" tdindex="73" or_wd="100" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""></td><td id="grdCompCmp_cell_18_2" readonly="true" inputtype="text" textalign="left" colindex="2" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_2_" style="text-align: left;" col_id="koreanNm" tdindex="74" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""></td><td id="grdCompCmp_cell_18_3" readonly="true" inputtype="text" textalign="left" colindex="3" role="gridcell" class="gridBodyDefault gridBodyDefault_data grdCompCmp_columnstyle_3_" style="text-align: left;" col_id="uCpnyNm" tdindex="75" or_wd="220" style_bak="text-align:left;text-align:left;unique:function()
{
  var a = {};
  for(var i=0; i<this.length; i++)
  {
	if(typeof a[this[i]] == &quot;undefined&quot;)
	  a[this[i]] = 1;
  }
  this.length = 0;
  for(var i in a)
	this[this.length] = i;
  return this;
}" or_bgcolor=""><nobr>한화자산운용</nobr></td></tr></tbody>
"""


soup     = BeautifulSoup(aaa, 'html.parser') #for development

for nobr in soup.find_all('nobr'):
    print nobr.get_text()
