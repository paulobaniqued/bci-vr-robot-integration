<?xml version='1.0' encoding='utf-8'?>
<scheme description="This pipeline predicts imagined motor actions using neural oscillatory pattern classification. The main node of this pipeline is the Common Spatial Pattern (CSP) filter, which is used to retrieve the components or patterns in the signal that are most suitable to represent desired categories or classes. CSP and its various extensions (available through NeuroPype) provide a powerful tool for building applications based on neural oscillations.&#10;This pipeline can be divided into 4 main parts, which we discuss in the following:&#10;&#10;Data acquisition:&#10;Includes : Import Data (here titled “Import SET”), LSL input/output, Stream Data and Inject Calibration Data nodes.&#10;In general you can process your data online or offline. For developing and testing purposes you will be mostly performing offline process using a pre-recorded file.&#10;&#10;- The “Import Data” nodes (here titled “Import Set”) are used to connect the pipeline to files.&#10;&#10;- The “LSL input” and “LSL output” nodes are used to get data stream into the pipeline, or send the data out to the network from the pipeline. (If you are sending markers make sure to check the “send marker” option in “LSL output” node)&#10;&#10;- The “Inject Calibration Data” node is used to pass the initial calibration data into the pipeline before the actual data is processed. The calibration data (Calib Data) is used by adaptive and machine learning algorithms to train and set their parameters initially. The main data is connected to the “Streaming Data” port.&#10;&#10;NOTE regarding “Inject Calibration Data”: &#10;In case you would like to train and test your pipeline using files (without using streaming node), you need to set the “Delay streaming packets” in this node. This enables the “Inject Calibration Data” node to buffer the test data that is pushed into it for one cycle and transfer it to the output port in the next cycle. It should be noted that the first cycle is used to push the calibration data through the pipeline.&#10;&#10;Data preprocess:&#10;Includes: Assign Targets, Select Range,  FIR filter and Segmentation nodes&#10;&#10;- The “Assign Target” node is mostly useful for the supervised learning algorithms, where  target values are assigned to specific markers present in the EEG signal. In order for this node to operate correctly you need to know the label for the markers in the data.&#10;&#10;- The “Select Range” node is used to specify certain parts of the data stream. For example, if we have a headset that contains certain bad channels, you can manually remove them here. That is the case for our example here where only data from the last 6 channels are used.&#10;&#10;- The “FIR Filter” node is used to remove the unwanted signals components outside of the EEG signal frequencies, e.g. to keep the 6-30 Hz frequency window.&#10;&#10;- The “Segmentation” node performs the epoching process, where the streamed data is divided into segments of the predefined window-length around the markers on the EEG data.&#10;&#10;NOTE regarding &quot;Segmentation&quot; node:&#10;The epoching process can be either done relative to the marker or the time window. When Processing a large file you should set the epoching relative to markers and while processing the streaming data, you should set it to sliding which chooses a single window at the end of the data.&#10;&#10;Feature extraction:&#10;&#10;Includes: Common Spatial Patterns (CSP) node&#10;As discussed above the spectral and spatial patterns in the data can be extracted by the CSP filters and its extensions.&#10;&#10;Classification:&#10;Includes: Variance, Logarithm, Logistic Regression and Measure Loss&#10;&#10;- The “Logistic Regression” node is used to perform the classification, where supervised learning methods is used to train the classifier. in this node you can choose the type of regularization and the regularization coefficient. You can also set the number of the folds for cross-validation in this node.&#10;&#10;- The “Measure Loss” node is used to measure various performance criteria. Here we use misclassification rate (MCR)." title="Simple Motor Imagery Prediction with CSP" version="2.0">
	<nodes>
		<node id="0" name="Assign Target Values" position="(500.0, 99.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="445a20d2-4258-4747-84e4-7b968057cc1e" version="1.0.0" />
		<node id="1" name="Segmentation" position="(300, 300)" project_name="NeuroPype" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" title="Segmentation" uuid="295e5b46-90a5-49f8-ab00-6360e43ad38a" version="1.0.1" />
		<node id="2" name="Common Spatial Patterns" position="(400, 300)" project_name="NeuroPype" qualified_name="widgets.neural.owcommonspatialpatterns.OWCommonSpatialPatterns" title="Common Spatial Patterns" uuid="c05727ba-bee7-4450-84d7-ce5ec8a139f9" version="1.0.0" />
		<node id="3" name="Variance" position="(500, 300)" project_name="NeuroPype" qualified_name="widgets.statistics.owvariance.OWVariance" title="Variance" uuid="5047f952-f40a-4d03-be13-5aaf5198f174" version="1.0.0" />
		<node id="4" name="Logarithm" position="(600, 300)" project_name="NeuroPype" qualified_name="widgets.elementwise_math.owlogarithm.OWLogarithm" title="Logarithm" uuid="53b815bc-c1db-45db-9d53-8702afe7e925" version="1.0.0" />
		<node id="5" name="Select Range" position="(600, 100)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="ee021b36-e07d-417d-abce-5992f31cc960" version="1.0.0" />
		<node id="6" name="Logistic Regression" position="(700, 300)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlogisticregression.OWLogisticRegression" title="Logistic Regression" uuid="dbfa8ebe-c9fd-4ebf-92e9-d7fca1bfceb9" version="1.0.0" />
		<node id="7" name="FIR Filter" position="(200, 300)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="f7713a0c-01a4-4e38-ab7a-400282fcc968" version="1.0.0" />
		<node id="8" name="LSL Input" position="(-94.0, 113.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="f5785705-eb96-44f7-8e79-8ca3cc6987d2" version="1.0.0" />
		<node id="9" name="Dejitter Timestamps" position="(200, 100)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="4846ced1-d781-46b1-8cc2-9a33f96e342d" version="1.0.0" />
		<node id="10" name="Inject Calibration Data" position="(400, 100)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owinjectcalibrationdata.OWInjectCalibrationData" title="Inject Calibration Data" uuid="e50200e2-6f93-4f0c-8dbd-468069db51a5" version="1.0.0" />
		<node id="11" name="Streaming Bar Plot" position="(933.0, 110.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="2ab70c7a-1736-4aaa-bd8e-82744629b9a1" version="1.0.2" />
		<node id="12" name="Print To Console" position="(966.0, 297.0)" project_name="NeuroPype" qualified_name="widgets.diagnostics.owprinttoconsole.OWPrintToConsole" title="Print To Console" uuid="3e16445d-1642-47b5-9616-e51ace312b3e" version="1.0.0" />
		<node id="13" name="Import XDF" position="(75.0, 25.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="6544e5b4-a2c9-4a0c-8343-8cdfadc64fa3" version="1.0.0" />
		<node id="14" name="Record to XDF" position="(-62.0, 302.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="10ced9cb-846a-4346-ab7f-4c001e6165d4" version="1.0.0" />
		<node id="15" name="Override Axis" position="(819.0, 190.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="07b93240-84d1-4841-a4bf-fa632a9121e6" version="1.0.2" />
		<node id="16" name="Rewrite Markers" position="(66.0, 136.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers" uuid="f5b23845-b51b-4c22-806c-2abca0e00d35" version="0.9.3" />
		<node id="17" name="Rewrite Markers" position="(219.0, 10.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers" uuid="3a20ddf0-f9e2-4b02-9f68-45d79cb18624" version="0.9.3" />
		<node id="18" name="Import XDF" position="(-72.0, 462.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owimportxdf.OWImportXDF" title="Import XDF" uuid="6c952400-a28d-433a-a18b-0d4952914995" version="1.0.0" />
		<node id="19" name="LSL Output" position="(262.0, 512.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output (1)" uuid="e15d89de-a6e1-4e7a-8021-e9b6777c69eb" version="1.0.0" />
		<node id="20" name="Stream Data" position="(74.0, 457.0)" project_name="NeuroPype" qualified_name="widgets.formatting.owstreamdata.OWStreamData" title="Stream Data" uuid="cb972687-ec97-494e-9c2e-0a11154c13a2" version="1.1.0" />
		<node id="21" name="Time Series Plot" position="(264.0, 432.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="b6c8fa6e-fac1-4fd1-b1bc-e70661f8232b" version="1.0.1" />
		<node id="22" name="LSL Output" position="(997.0, 199.0)" project_name="NeuroPype" qualified_name="widgets.network.owlsloutput.OWLSLOutput" title="LSL Output" uuid="df1560fa-d191-421b-aebf-e91ac9f39f75" version="1.0.0" />
		<node id="23" name="Override Axis" position="(804.0, 437.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owoverrideaxis.OWOverrideAxis" title="Override Axis" uuid="35e94774-6df4-4fa2-b504-66a97e816bb0" version="1.0.2" />
		<node id="24" name="Streaming Bar Plot" position="(947.0, 391.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owbarplot.OWBarPlot" title="Streaming Bar Plot" uuid="fee80da5-51bf-4772-ab41-26740462695f" version="1.0.2" />
		<node id="25" name="Linear Discriminant Analysis" position="(696.0, 432.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owlineardiscriminantanalysis.OWLinearDiscriminantAnalysis" title="Linear Discriminant Analysis" uuid="7695ca49-679d-455a-ae33-9b4e22fa6982" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="1" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="2" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="5" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="7" sink_channel="Streaming Data" sink_node_id="10" source_channel="Data" source_node_id="9" />
		<link enabled="true" id="8" sink_channel="Data" sink_node_id="0" source_channel="Data" source_node_id="10" />
		<link enabled="false" id="9" sink_channel="Data" sink_node_id="14" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="10" sink_channel="Data" sink_node_id="15" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="11" sink_channel="Data" sink_node_id="11" source_channel="Data" source_node_id="15" />
		<link enabled="true" id="12" sink_channel="Data" sink_node_id="16" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="13" sink_channel="Data" sink_node_id="9" source_channel="Data" source_node_id="16" />
		<link enabled="true" id="14" sink_channel="Data" sink_node_id="17" source_channel="Data" source_node_id="13" />
		<link enabled="true" id="15" sink_channel="Calib Data" sink_node_id="10" source_channel="Data" source_node_id="17" />
		<link enabled="true" id="16" sink_channel="Data" sink_node_id="20" source_channel="Data" source_node_id="18" />
		<link enabled="true" id="17" sink_channel="Data" sink_node_id="19" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="18" sink_channel="Data" sink_node_id="21" source_channel="Data" source_node_id="20" />
		<link enabled="true" id="19" sink_channel="Data" sink_node_id="24" source_channel="Data" source_node_id="23" />
		<link enabled="false" id="20" sink_channel="Data" sink_node_id="25" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="21" sink_channel="Data" sink_node_id="23" source_channel="Data" source_node_id="25" />
		<link enabled="true" id="22" sink_channel="Data" sink_node_id="22" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="23" sink_channel="Data" sink_node_id="12" source_channel="Data" source_node_id="6" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWBIAAABhbHNvX2xlZ2FjeV9vdXRwdXRxAYlYDgAAAGlzX2NhdGVnb3JpY2FscQKJWAkA
AABpdl9jb2x1bW5xA1gGAAAATWFya2VycQRYBwAAAG1hcHBpbmdxBX1xBihYBAAAAGxlZnRxB0sA
WAUAAAByaWdodHEISwF1WA4AAABtYXBwaW5nX2Zvcm1hdHEJWAYAAABjb21wYXRxClgTAAAAc2F2
ZWRXaWRnZXRHZW9tZXRyeXELY3NpcApfdW5waWNrbGVfdHlwZQpxDFgMAAAAUHlRdDQuUXRDb3Jl
cQ1YCgAAAFFCeXRlQXJyYXlxDkMuAdnQywABAAAAAAAAAAACGgAAAXcAAAMhAAAACAAAAjkAAAFv
AAADGQAAAAAAAHEPhXEQh3ERUnESWA4AAABzZXRfYnJlYWtwb2ludHETiVgRAAAAc3VwcG9ydF93
aWxkY2FyZHNxFIlYCwAAAHVzZV9udW1iZXJzcRWJWAcAAAB2ZXJib3NlcRaJdS4=
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWBEAAABrZWVwX21hcmtlcl9jaHVua3EBiVgOAAAAbWF4X2dhcF9sZW5ndGhxAkc/yZmZ
mZmZmlgPAAAAb25saW5lX2Vwb2NoaW5ncQNYDQAAAG1hcmtlci1sb2NrZWRxBFgNAAAAc2FtcGxl
X29mZnNldHEFSwBYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBmNzaXAKX3VucGlja2xlX3R5cGUK
cQdYDAAAAFB5UXQ0LlF0Q29yZXEIWAoAAABRQnl0ZUFycmF5cQlDLgHZ0MsAAQAAAAABYwAAAiAA
AALaAAADGAAAAWsAAAI/AAAC0gAAAxAAAAAAAABxCoVxC4dxDFJxDVgOAAAAc2VsZWN0X21hcmtl
cnNxDlgNAAAAKHVzZSBkZWZhdWx0KXEPWA4AAABzZXRfYnJlYWtwb2ludHEQiVgLAAAAdGltZV9i
b3VuZHNxEV1xEihLAEsEZVgHAAAAdmVyYm9zZXETiXUu
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAoAAABjb25kX2ZpZWxkcQFYCwAAAFRhcmdldFZhbHVlcQJYDwAAAGluaXRpYWxpemVf
b25jZXEDiFgDAAAAbm9mcQRLA1gTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEFY3NpcApfdW5waWNr
bGVfdHlwZQpxBlgMAAAAUHlRdDQuUXRDb3JlcQdYCgAAAFFCeXRlQXJyYXlxCEMuAdnQywABAAAA
AAMEAAABuQAABHsAAAI/AAADDAAAAdgAAARzAAACNwAAAAAAAHEJhXEKh3ELUnEMWA4AAABzZXRf
YnJlYWtwb2ludHENiXUu
</properties>
		<properties format="pickle" node_id="3">gAN9cQAoWAQAAABheGlzcQFYBAAAAHRpbWVxAlgSAAAAZGVncmVlc19vZl9mcmVlZG9tcQNLAFgS
AAAAZm9yY2VfZmVhdHVyZV9heGlzcQSJWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQVjc2lwCl91
bnBpY2tsZV90eXBlCnEGWAwAAABQeVF0NC5RdENvcmVxB1gKAAAAUUJ5dGVBcnJheXEIQy4B2dDL
AAEAAP///ogAAAJX/////wAAAwr///6QAAACdv////cAAAMCAAAAAQAAcQmFcQqHcQtScQxYDgAA
AHNldF9icmVha3BvaW50cQ2JdS4=
</properties>
		<properties format="pickle" node_id="4">gAN9cQAoWAQAAABiYXNlcQFYDQAAACh1c2UgZGVmYXVsdClxAlgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXEDY3NpcApfdW5waWNrbGVfdHlwZQpxBFgMAAAAUHlRdDQuUXRDb3JlcQVYCgAAAFFCeXRl
QXJyYXlxBkMuAdnQywABAAAAAAMEAAABuQAABHsAAAI/AAADDAAAAdgAAARzAAACNwAAAAAAAHEH
hXEIh3EJUnEKWA4AAABzZXRfYnJlYWtwb2ludHELiXUu
</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWBMAAABhcHBseV9tdWx0aXBsZV9heGVzcQGJWAQAAABheGlzcQJYBQAAAHNwYWNlcQNY
EwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxBGNzaXAKX3VucGlja2xlX3R5cGUKcQVYDAAAAFB5UXQ0
LlF0Q29yZXEGWAoAAABRQnl0ZUFycmF5cQdDLgHZ0MsAAQAAAAABZQAAAv8AAALcAAADygAAAW0A
AAMeAAAC1AAAA8IAAAAAAABxCIVxCYdxClJxC1gJAAAAc2VsZWN0aW9ucQxYAwAAADA6OHENWA4A
AABzZXRfYnJlYWtwb2ludHEOiVgEAAAAdW5pdHEPWAcAAABpbmRpY2VzcRB1Lg==
</properties>
		<properties format="pickle" node_id="6">gAN9cQAoWAYAAABhbHBoYXNxAV1xAihHP7mZmZmZmZpHP+AAAAAAAABHP/AAAAAAAABLBUdAJAAA
AAAAAGVYDAAAAGJpYXNfc2NhbGluZ3EDRz/wAAAAAAAAWA0AAABjbGFzc193ZWlnaHRzcQRYBAAA
AGF1dG9xBVgKAAAAY29uZF9maWVsZHEGWAsAAABUYXJnZXRWYWx1ZXEHWBAAAABkb250X3Jlc2V0
X21vZGVscQiJWBAAAABkdWFsX2Zvcm11bGF0aW9ucQmJWAwAAABpbmNsdWRlX2JpYXNxCohYDwAA
AGluaXRpYWxpemVfb25jZXELiFgIAAAAbWF4X2l0ZXJxDEtkWAoAAABtdWx0aWNsYXNzcQ1YAwAA
AG92cnEOWAkAAABudW1fZm9sZHNxD0sFWAgAAABudW1fam9ic3EQSwFYDQAAAHByb2JhYmlsaXN0
aWNxEYhYCwAAAHJlZ3VsYXJpemVycRJYAgAAAGwycRNYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlx
FGNzaXAKX3VucGlja2xlX3R5cGUKcRVYDAAAAFB5UXQ0LlF0Q29yZXEWWAoAAABRQnl0ZUFycmF5
cRdDLgHZ0MsAAQAAAAADBAAAAYsAAAR7AAACbgAAAwwAAAGqAAAEcwAAAmYAAAAAAABxGIVxGYdx
GlJxG1gNAAAAc2VhcmNoX21ldHJpY3EcWAgAAABhY2N1cmFjeXEdWA4AAABzZXRfYnJlYWtwb2lu
dHEeiVgGAAAAc29sdmVycR9YBQAAAGxiZmdzcSBYCQAAAHRvbGVyYW5jZXEhRz8aNuLrHEMtWAkA
AAB2ZXJib3NpdHlxIksAdS4=
</properties>
		<properties format="pickle" node_id="7">gAN9cQAoWA0AAABhbnRpc3ltbWV0cmljcQGJWAQAAABheGlzcQJYBAAAAHRpbWVxA1gSAAAAY29u
dm9sdXRpb25fbWV0aG9kcQRYCAAAAHN0YW5kYXJkcQVYDgAAAGN1dF9wcmVyaW5naW5ncQaJWAsA
AABmcmVxdWVuY2llc3EHXXEIKEsGSwdLHksgZVgNAAAAbWluaW11bV9waGFzZXEJiFgEAAAAbW9k
ZXEKWAgAAABiYW5kcGFzc3ELWAUAAABvcmRlcnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEwAAAHNh
dmVkV2lkZ2V0R2VvbWV0cnlxDmNzaXAKX3VucGlja2xlX3R5cGUKcQ9YDAAAAFB5UXQ0LlF0Q29y
ZXEQWAoAAABRQnl0ZUFycmF5cRFDLgHZ0MsAAQAAAAADDAAAAYYAAASDAAACsAAAAxQAAAGlAAAE
ewAAAqgAAAAAAABxEoVxE4dxFFJxFVgOAAAAc2V0X2JyZWFrcG9pbnRxFolYCgAAAHN0b3BfYXR0
ZW5xF0dASQAAAAAAAHUu
</properties>
		<properties format="pickle" node_id="8">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgOAAAAdHlwZT0nTWFya2VycydxBVgMAAAAbWF4X2Jsb2NrbGVucQZNAARYCgAA
AG1heF9idWZsZW5xB0seWAwAAABtYXhfY2h1bmtsZW5xCEsAWAwAAABub21pbmFsX3JhdGVxCVgN
AAAAKHVzZSBkZWZhdWx0KXEKWAUAAABxdWVyeXELWAoAAAB0eXBlPSdFRUcncQxYBwAAAHJlY292
ZXJxDYhYFAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5HP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0
R2VvbWV0cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABR
Qnl0ZUFycmF5cRJDLgHZ0MsAAQAAAAABtQAAAYIAAAMsAAAC7wAAAb0AAAGhAAADJAAAAucAAAAA
AABxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="9">gAN9cQAoWA8AAABmb3JjZV9tb25vdG9uaWNxAYhYDwAAAGZvcmdldF9oYWxmdGltZXECTSwBWA4A
AABtYXhfdXBkYXRlcmF0ZXEDTfQBWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQRjc2lwCl91bnBp
Y2tsZV90eXBlCnEFWAwAAABQeVF0NC5RdENvcmVxBlgKAAAAUUJ5dGVBcnJheXEHQy4B2dDLAAEA
AAAABEgAAAI/AAAFvwAAAyUAAARQAAACXgAABbcAAAMdAAAAAAAAcQiFcQmHcQpScQtYDgAAAHNl
dF9icmVha3BvaW50cQyJWA4AAAB3YXJtdXBfc2FtcGxlc3ENSv////91Lg==
</properties>
		<properties format="pickle" node_id="10">gAN9cQAoWBcAAABkZWxheV9zdHJlYW1pbmdfcGFja2V0c3EBiFgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXECY3NpcApfdW5waWNrbGVfdHlwZQpxA1gMAAAAUHlRdDQuUXRDb3JlcQRYCgAAAFFCeXRl
QXJyYXlxBUMuAdnQywABAAAAAAMEAAABuwAABHsAAAI+AAADDAAAAdoAAARzAAACNgAAAAAAAHEG
hXEHh3EIUnEJWA4AAABzZXRfYnJlYWtwb2ludHEKiXUu
</properties>
		<properties format="pickle" node_id="11">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/VHrhR64UfWAwAAABpbml0aWFsX2RpbXNxCV1xCihLMksyTbwCTfQB
ZVgOAAAAaW5zdGFuY2VfZmllbGRxC1gNAAAAKHVzZSBkZWZhdWx0KXEMWA4AAABsYWJlbF9yb3Rh
dGlvbnENWAgAAAB2ZXJ0aWNhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBp
Y2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEA
AAAAAwQAAAFEAAAEewAAAyAAAAMMAAABYwAABHMAAAMYAAAAAAAAcROFcRSHcRVScRZYDgAAAHNl
dF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRloDFgF
AAAAdGl0bGVxGlgTAAAATG9naXN0aWMgUmVncmVzc2lvbnEbWBEAAAB1c2VfbGFzdF9pbnN0YW5j
ZXEciFgHAAAAdmVyYm9zZXEdiVgIAAAAeV9saW1pdHNxHl1xHyhLAEsBZXUu
</properties>
		<properties format="pickle" node_id="12">gAN9cQAoWA0AAABvbmx5X25vbmVtcHR5cQGIWA0AAABwcmludF9jaGFubmVscQKJWA0AAABwcmlu
dF9jb21wYWN0cQOJWAoAAABwcmludF9kYXRhcQSIWA0AAABwcmludF9tYXJrZXJzcQWJWA0AAABw
cmludF9zdHJlYW1zcQZdcQdYCgAAAHByaW50X3RpbWVxCIlYCwAAAHByaW50X3RyaWFscQmJWBMA
AABzYXZlZFdpZGdldEdlb21ldHJ5cQpjc2lwCl91bnBpY2tsZV90eXBlCnELWAwAAABQeVF0NC5R
dENvcmVxDFgKAAAAUUJ5dGVBcnJheXENQy4B2dDLAAEAAAAAAwAAAAHtAAAEdwAAAwYAAAMIAAAC
DAAABG8AAAL+AAAAAAAAcQ6FcQ+HcRBScRFYDgAAAHNldF9icmVha3BvaW50cRKJdS4=
</properties>
		<properties format="pickle" node_id="13">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBoAAABFOi9iY2kvcGlwZWxpbmUvdGVzdC0xLnhkZnEIWBMAAABoYW5kbGVf
Y2xvY2tfcmVzZXRzcQmIWBEAAABoYW5kbGVfY2xvY2tfc3luY3EKiFgVAAAAaGFuZGxlX2ppdHRl
cl9yZW1vdmFscQuIWA4AAABtYXhfbWFya2VyX2xlbnEMWA0AAAAodXNlIGRlZmF1bHQpcQ1YEgAA
AHJlb3JkZXJfdGltZXN0YW1wc3EOiVgOAAAAcmV0YWluX3N0cmVhbXNxD2gNWBMAAABzYXZlZFdp
ZGdldEdlb21ldHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NC5RdENvcmVxElgK
AAAAUUJ5dGVBcnJheXETQy4B2dDLAAEAAAAAAwQAAAF9AAAEewAAAnsAAAMMAAABnAAABHMAAAJz
AAAAAAAAcRSFcRWHcRZScRdYDgAAAHNldF9icmVha3BvaW50cRiJWA8AAAB1c2Vfc3RyZWFtbmFt
ZXNxGYlYBwAAAHZlcmJvc2VxGol1Lg==
</properties>
		<properties format="pickle" node_id="14">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYGgAAAEU6L2JjaS9waXBlbGluZS90ZXN0LTIueGRmcQ1YCwAAAG91dHB1dF9yb290cQ5o
BVgLAAAAcmV0cmlldmFibGVxD4lYEwAAAHNhdmVkV2lkZ2V0R2VvbWV0cnlxEGNzaXAKX3VucGlj
a2xlX3R5cGUKcRFYDAAAAFB5UXQ0LlF0Q29yZXESWAoAAABRQnl0ZUFycmF5cRNDLgHZ0MsAAQAA
AAADBAAAAUQAAAR7AAACtAAAAwwAAAFjAAAEcwAAAqwAAAAAAABxFIVxFYdxFlJxF1gNAAAAc2Vz
c2lvbl9ub3Rlc3EYaAVYDgAAAHNldF9icmVha3BvaW50cRmJWAcAAAB2ZXJib3NlcRqJdS4=
</properties>
		<properties format="pickle" node_id="15">gAN9cQAoWA8AAABheGlzX29jY3VycmVuY2VxAUsAWBAAAABjYXJyeV9vdmVyX25hbWVzcQKIWBIA
AABjYXJyeV9vdmVyX251bWJlcnNxA4hYDAAAAGN1c3RvbV9sYWJlbHEEWA0AAAAodXNlIGRlZmF1
bHQpcQVYCQAAAGluaXRfZGF0YXEGXXEHKFgEAAAAbGVmdHEIWAUAAAByaWdodHEJZVgIAAAAbmV3
X2F4aXNxClgHAAAAZmVhdHVyZXELWAgAAABvbGRfYXhpc3EMWAcAAABmZWF0dXJlcQ1YDAAAAG9u
bHlfc2lnbmFsc3EOiFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEPY3NpcApfdW5waWNrbGVfdHlw
ZQpxEFgMAAAAUHlRdDQuUXRDb3JlcRFYCgAAAFFCeXRlQXJyYXlxEkMuAdnQywABAAAAAAMEAAAB
gAAABHsAAAKTAAADDAAAAZ8AAARzAAACiwAAAAAAAHEThXEUh3EVUnEWWA4AAABzZXRfYnJlYWtw
b2ludHEXiXUu
</properties>
		<properties format="pickle" node_id="16">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaI
WAUAAABydWxlc3EHWBsAAAB7JzMnOiAnbGVmdCcsICc0JzogJ3JpZ2h0J31xCFgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEJY3NpcApfdW5waWNrbGVfdHlwZQpxClgMAAAAUHlRdDQuUXRDb3JlcQtY
CgAAAFFCeXRlQXJyYXlxDEMuAdnQywABAAAAAAMEAAABowAABHsAAAJWAAADDAAAAcIAAARzAAAC
TgAAAAAAAHENhXEOh3EPUnEQWA4AAABzZXRfYnJlYWtwb2ludHERiXUu
</properties>
		<properties format="pickle" node_id="17">gAN9cQAoWAkAAABpdl9jb2x1bW5xAVgGAAAATWFya2VycQJYDgAAAHBhdHRlcm5fc3ludGF4cQNY
CQAAAHdpbGRjYXJkc3EEWAkAAAByZWdleF9zdWJxBYlYEQAAAHJlbW92ZV9hbGxfb3RoZXJzcQaI
WAUAAABydWxlc3EHWBsAAAB7JzMnOiAnbGVmdCcsICc0JzogJ3JpZ2h0J31xCFgTAAAAc2F2ZWRX
aWRnZXRHZW9tZXRyeXEJY3NpcApfdW5waWNrbGVfdHlwZQpxClgMAAAAUHlRdDQuUXRDb3JlcQtY
CgAAAFFCeXRlQXJyYXlxDEMuAdnQywABAAAAAAMEAAABowAABHsAAAJWAAADDAAAAcIAAARzAAAC
TgAAAAAAAHENhXEOh3EPUnEQWA4AAABzZXRfYnJlYWtwb2ludHERiXUu
</properties>
		<properties format="pickle" node_id="18">gAN9cQAoWA0AAABjbG91ZF9hY2NvdW50cQFYAAAAAHECWAwAAABjbG91ZF9idWNrZXRxA2gCWBEA
AABjbG91ZF9jcmVkZW50aWFsc3EEaAJYCgAAAGNsb3VkX2hvc3RxBVgHAAAARGVmYXVsdHEGWAgA
AABmaWxlbmFtZXEHWBsAAABFOi9iY2kvcGlwZWxpbmUvdHJhaW4tMS54ZGZxCFgTAAAAaGFuZGxl
X2Nsb2NrX3Jlc2V0c3EJiFgRAAAAaGFuZGxlX2Nsb2NrX3N5bmNxCohYFQAAAGhhbmRsZV9qaXR0
ZXJfcmVtb3ZhbHELiFgOAAAAbWF4X21hcmtlcl9sZW5xDFgNAAAAKHVzZSBkZWZhdWx0KXENWBIA
AAByZW9yZGVyX3RpbWVzdGFtcHNxDolYDgAAAHJldGFpbl9zdHJlYW1zcQ9YDQAAACh1c2UgZGVm
YXVsdClxEFgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXERY3NpcApfdW5waWNrbGVfdHlwZQpxElgM
AAAAUHlRdDQuUXRDb3JlcRNYCgAAAFFCeXRlQXJyYXlxFEMuAdnQywABAAAAAAMEAAABfQAABHsA
AAJ7AAADDAAAAZwAAARzAAACcwAAAAAAAHEVhXEWh3EXUnEYWA4AAABzZXRfYnJlYWtwb2ludHEZ
iVgPAAAAdXNlX3N0cmVhbW5hbWVzcRqJWAcAAAB2ZXJib3NlcRuJdS4=
</properties>
		<properties format="pickle" node_id="19">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYCwAAAGN1ZV9tYXJrZXJzcQRYEAAAAG1hcmtlcl9zb3VyY2VfaWRxBVgA
AAAAcQZYDAAAAG1heF9idWZmZXJlZHEHSzxYFwAAAHJlc2V0X2lmX2xhYmVsc19jaGFuZ2VkcQiJ
WBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQljc2lwCl91bnBpY2tsZV90eXBlCnEKWAwAAABQeVF0
NC5RdENvcmVxC1gKAAAAUUJ5dGVBcnJheXEMQy4B2dDLAAEAAAAAAwQAAAE9AAAEewAAArwAAAMM
AAABXAAABHMAAAK0AAAAAAAAcQ2FcQ6HcQ9ScRBYDAAAAHNlbmRfbWFya2Vyc3ERiFgOAAAAc2V0
X2JyZWFrcG9pbnRxEolYCQAAAHNvdXJjZV9pZHETaAZYBQAAAHNyYXRlcRRYDQAAACh1c2UgZGVm
YXVsdClxFVgLAAAAc3RyZWFtX25hbWVxFlgDAAAARUVHcRdYCwAAAHN0cmVhbV90eXBlcRhYAwAA
AEVFR3EZWBMAAAB1c2VfZGF0YV90aW1lc3RhbXBzcRqIWBYAAAB1c2VfbnVtcHlfb3B0aW1pemF0
aW9ucRuJdS4=
</properties>
		<properties format="pickle" node_id="20">gAN9cQAoWBEAAABoaXRjaF9wcm9iYWJpbGl0eXEBRwAAAAAAAAAAWA4AAABqaXR0ZXJfcGVyY2Vu
dHECSwVYBwAAAGxvb3BpbmdxA4hYCAAAAHJhbmRzZWVkcQRN54ZYEwAAAHNhdmVkV2lkZ2V0R2Vv
bWV0cnlxBWNzaXAKX3VucGlja2xlX3R5cGUKcQZYDAAAAFB5UXQ0LlF0Q29yZXEHWAoAAABRQnl0
ZUFycmF5cQhDLgHZ0MsAAQAAAAADBAAAAWcAAAR7AAACkgAAAwwAAAGGAAAEcwAAAooAAAAAAABx
CYVxCodxC1JxDFgOAAAAc2V0X2JyZWFrcG9pbnRxDYlYBwAAAHNwZWVkdXBxDkc/8AAAAAAAAFgJ
AAAAc3RhcnRfcG9zcQ9HAAAAAAAAAABYEAAAAHRpbWVzdGFtcF9qaXR0ZXJxEEcAAAAAAAAAAFgG
AAAAdGltaW5ncRFYCQAAAHdhbGxjbG9ja3ESWA8AAAB1cGRhdGVfaW50ZXJ2YWxxE0c/pHrhR64U
e3Uu
</properties>
		<properties format="pickle" node_id="21">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReJWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAwQAAAE1AAAEewAAAsMAAAMMAAABVAAABHMA
AAK7AAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIolYCwAAAHN0cmVhbV9uYW1lcSNoFVgKAAAAdGltZV9y
YW5nZXEkR0AkAAAAAAAAWAUAAAB0aXRsZXElWBAAAABUaW1lIHNlcmllcyB2aWV3cSZYCgAAAHpl
cm9fY29sb3JxJ1gHAAAAIzdGN0Y3RnEoWAgAAAB6ZXJvbWVhbnEpiHUu
</properties>
		<properties format="pickle" node_id="22">gAN9cQAoWAkAAABjaHVua19sZW5xAUsAWBUAAABpZ25vcmVfc2lnbmFsX2NoYW5nZWRxAolYCwAA
AG1hcmtlcl9uYW1lcQNYEgAAAHByZWRpY3Rpb25fbWFya2Vyc3EEWBAAAABtYXJrZXJfc291cmNl
X2lkcQVYAAAAAHEGWAwAAABtYXhfYnVmZmVyZWRxB0s8WBcAAAByZXNldF9pZl9sYWJlbHNfY2hh
bmdlZHEIiVgTAAAAc2F2ZWRXaWRnZXRHZW9tZXRyeXEJY3NpcApfdW5waWNrbGVfdHlwZQpxClgM
AAAAUHlRdDQuUXRDb3JlcQtYCgAAAFFCeXRlQXJyYXlxDEMuAdnQywABAAAAAAMMAAABWwAABIMA
AALaAAADFAAAAXoAAAR7AAAC0gAAAAAAAHENhXEOh3EPUnEQWAwAAABzZW5kX21hcmtlcnNxEYlY
DgAAAHNldF9icmVha3BvaW50cRKJWAkAAABzb3VyY2VfaWRxE1g+AAAAKG1ha2Ugc3VyZSB0byBu
ZXZlciB1c2Ugc2FtZSBzdHJpbmcgbW9yZSB0aGFuIG9uY2Ugb24gbmV0d29yaylxFFgFAAAAc3Jh
dGVxFVgNAAAAKHVzZSBkZWZhdWx0KXEWWAsAAABzdHJlYW1fbmFtZXEXWAoAAABQcmVkaWN0aW9u
cRhYCwAAAHN0cmVhbV90eXBlcRlYCgAAAFByZWRpY3Rpb25xGlgTAAAAdXNlX2RhdGFfdGltZXN0
YW1wc3EbiFgWAAAAdXNlX251bXB5X29wdGltaXphdGlvbnEciXUu
</properties>
		<properties format="literal" node_id="23">{'axis_occurrence': 0, 'carry_over_names': True, 'carry_over_numbers': True, 'custom_label': '(use default)', 'init_data': ['left', 'right'], 'new_axis': 'feature', 'old_axis': 'feature', 'only_signals': True, 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="24">gAN9cQAoWA0AAABhbHdheXNfb25fdG9wcQGJWAQAAABheGlzcQJYBwAAAGZlYXR1cmVxA1gQAAAA
YmFja2dyb3VuZF9jb2xvcnEEWAcAAAAjRkZGRkZGcQVYCQAAAGJhcl9jb2xvcnEGWAEAAABicQdY
CQAAAGJhcl93aWR0aHEIRz/VHrhR64UfWAwAAABpbml0aWFsX2RpbXNxCV1xCihLMksyTbwCTfQB
ZVgOAAAAaW5zdGFuY2VfZmllbGRxC1gNAAAAKHVzZSBkZWZhdWx0KXEMWA4AAABsYWJlbF9yb3Rh
dGlvbnENWAgAAAB2ZXJ0aWNhbHEOWBMAAABzYXZlZFdpZGdldEdlb21ldHJ5cQ9jc2lwCl91bnBp
Y2tsZV90eXBlCnEQWAwAAABQeVF0NC5RdENvcmVxEVgKAAAAUUJ5dGVBcnJheXESQy4B2dDLAAEA
AAAAAwQAAAFSAAAEewAAAqcAAAMMAAABcQAABHMAAAKfAAAAAAAAcROFcRSHcRVScRZYDgAAAHNl
dF9icmVha3BvaW50cReJWAwAAABzaG93X3Rvb2xiYXJxGIlYCwAAAHN0cmVhbV9uYW1lcRlYDQAA
ACh1c2UgZGVmYXVsdClxGlgFAAAAdGl0bGVxG1gDAAAATERBcRxYEQAAAHVzZV9sYXN0X2luc3Rh
bmNlcR2IWAcAAAB2ZXJib3NlcR6JWAgAAAB5X2xpbWl0c3EfXXEgKEsASwFldS4=
</properties>
		<properties format="pickle" node_id="25">gAN9cQAoWA0AAABjbGFzc193ZWlnaHRzcQFYDQAAACh1c2UgZGVmYXVsdClxAlgKAAAAY29uZF9m
aWVsZHEDWAsAAABUYXJnZXRWYWx1ZXEEWBAAAABkb250X3Jlc2V0X21vZGVscQWJWA8AAABpbml0
aWFsaXplX29uY2VxBohYCQAAAG51bV9mb2xkc3EHSwVYDQAAAHByb2JhYmlsaXN0aWNxCIhYEwAA
AHNhdmVkV2lkZ2V0R2VvbWV0cnlxCWNzaXAKX3VucGlja2xlX3R5cGUKcQpYDAAAAFB5UXQ0LlF0
Q29yZXELWAoAAABRQnl0ZUFycmF5cQxDLgHZ0MsAAQAAAAADBAAAAa8AAAR7AAACSgAAAwwAAAHO
AAAEcwAAAkIAAAAAAABxDYVxDodxD1JxEFgNAAAAc2VhcmNoX21ldHJpY3ERWAgAAABhY2N1cmFj
eXESWA4AAABzZXRfYnJlYWtwb2ludHETiVgJAAAAc2hyaW5rYWdlcRRYBAAAAGF1dG9xFVgGAAAA
c29sdmVycRZYBQAAAGVpZ2VucRdYCQAAAHRvbGVyYW5jZXEYRz8aNuLrHEMtWAkAAAB2ZXJib3Np
dHlxGUsAdS4=
</properties>
	</node_properties>
	<patch>{
    "description": {
        "description": "(description missing)",
        "license": "",
        "name": "(untitled)",
        "status": "(unspecified)",
        "url": "",
        "version": "0.0.0"
    },
    "edges": [
        [
            "node2",
            "data",
            "node3",
            "data"
        ],
        [
            "node3",
            "data",
            "node4",
            "data"
        ],
        [
            "node4",
            "data",
            "node5",
            "data"
        ],
        [
            "node1",
            "data",
            "node6",
            "data"
        ],
        [
            "node5",
            "data",
            "node7",
            "data"
        ],
        [
            "node6",
            "data",
            "node8",
            "data"
        ],
        [
            "node8",
            "data",
            "node2",
            "data"
        ],
        [
            "node10",
            "data",
            "node11",
            "streaming_data"
        ],
        [
            "node11",
            "data",
            "node1",
            "data"
        ],
        [
            "node7",
            "data",
            "node16",
            "data"
        ],
        [
            "node7",
            "data",
            "node23",
            "data"
        ],
        [
            "node7",
            "data",
            "node13",
            "data"
        ],
        [
            "node16",
            "data",
            "node12",
            "data"
        ],
        [
            "node9",
            "data",
            "node17",
            "data"
        ],
        [
            "node17",
            "data",
            "node10",
            "data"
        ],
        [
            "node14",
            "data",
            "node18",
            "data"
        ],
        [
            "node18",
            "data",
            "node11",
            "calib_data"
        ],
        [
            "node19",
            "data",
            "node21",
            "data"
        ],
        [
            "node21",
            "data",
            "node20",
            "data"
        ],
        [
            "node21",
            "data",
            "node22",
            "data"
        ],
        [
            "node24",
            "data",
            "node25",
            "data"
        ],
        [
            "node26",
            "data",
            "node24",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "AssignTargets",
            "module": "neuropype.nodes.machine_learning.AssignTargets",
            "params": {
                "also_legacy_output": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "is_categorical": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "mapping": {
                    "customized": true,
                    "type": "Port",
                    "value": {
                        "left": 0,
                        "right": 1
                    }
                },
                "mapping_format": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "compat"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "support_wildcards": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_numbers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "445a20d2-4258-4747-84e4-7b968057cc1e"
        },
        "node10": {
            "class": "DejitterTimestamps",
            "module": "neuropype.nodes.utilities.DejitterTimestamps",
            "params": {
                "force_monotonic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "forget_halftime": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 300
                },
                "max_updaterate": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 500
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "warmup_samples": {
                    "customized": false,
                    "type": "IntPort",
                    "value": -1
                }
            },
            "uuid": "4846ced1-d781-46b1-8cc2-9a33f96e342d"
        },
        "node11": {
            "class": "InjectCalibrationData",
            "module": "neuropype.nodes.machine_learning.InjectCalibrationData",
            "params": {
                "delay_streaming_packets": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e50200e2-6f93-4f0c-8dbd-468069db51a5"
        },
        "node12": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.33
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "vertical"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Logistic Regression"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "2ab70c7a-1736-4aaa-bd8e-82744629b9a1"
        },
        "node13": {
            "class": "PrintToConsole",
            "module": "neuropype.nodes.diagnostics.PrintToConsole",
            "params": {
                "only_nonempty": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "print_channel": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_compact": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": false
                },
                "print_data": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "print_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_streams": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
                },
                "print_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "print_trial": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "3e16445d-1642-47b5-9616-e51ace312b3e"
        },
        "node14": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/bci/pipeline/test-1.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "6544e5b4-a2c9-4a0c-8343-8cdfadc64fa3"
        },
        "node15": {
            "class": "RecordToXDF",
            "module": "neuropype.nodes.file_system.RecordToXDF",
            "params": {
                "allow_double": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "close_on_marker": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "close-recording"
                },
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "cloud_partsize": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "delete_parts": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/bci/pipeline/test-2.xdf"
                },
                "output_root": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "retrievable": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "session_notes": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "10ced9cb-846a-4346-ab7f-4c001e6165d4"
        },
        "node16": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "left",
                        "right"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "07b93240-84d1-4841-a4bf-fa632a9121e6"
        },
        "node17": {
            "class": "RewriteMarkers",
            "module": "neuropype.nodes.markers.RewriteMarkers",
            "params": {
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "pattern_syntax": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wildcards"
                },
                "regex_sub": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "remove_all_others": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "rules": {
                    "customized": true,
                    "type": "Port",
                    "value": "{'3': 'left', '4': 'right'}"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f5b23845-b51b-4c22-806c-2abca0e00d35"
        },
        "node18": {
            "class": "RewriteMarkers",
            "module": "neuropype.nodes.markers.RewriteMarkers",
            "params": {
                "iv_column": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Marker"
                },
                "pattern_syntax": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wildcards"
                },
                "regex_sub": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "remove_all_others": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "rules": {
                    "customized": true,
                    "type": "Port",
                    "value": "{'3': 'left', '4': 'right'}"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "3a20ddf0-f9e2-4b02-9f68-45d79cb18624"
        },
        "node19": {
            "class": "ImportXDF",
            "module": "neuropype.nodes.file_system.ImportXDF",
            "params": {
                "cloud_account": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_bucket": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_credentials": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "cloud_host": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "Default"
                },
                "filename": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/bci/pipeline/train-1.xdf"
                },
                "handle_clock_resets": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_clock_sync": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "handle_jitter_removal": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_marker_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "reorder_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "retain_streams": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "use_streamnames": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "6c952400-a28d-433a-a18b-0d4952914995"
        },
        "node2": {
            "class": "Segmentation",
            "module": "neuropype.nodes.formatting.Segmentation",
            "params": {
                "keep_marker_chunk": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "max_gap_length": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.2
                },
                "online_epoching": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "marker-locked"
                },
                "sample_offset": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "select_markers": {
                    "customized": false,
                    "type": "ListPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "time_bounds": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        4
                    ]
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "295e5b46-90a5-49f8-ab00-6360e43ad38a"
        },
        "node20": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "cue_markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "EEG"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e15d89de-a6e1-4e7a-8021-e9b6777c69eb"
        },
        "node21": {
            "class": "StreamData",
            "module": "neuropype.nodes.formatting.StreamData",
            "params": {
                "hitch_probability": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "jitter_percent": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 5
                },
                "looping": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "randseed": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 34535
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "speedup": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "start_pos": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timestamp_jitter": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0
                },
                "timing": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "wallclock"
                },
                "update_interval": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.04
                }
            },
            "uuid": "cb972687-ec97-494e-9c2e-0a11154c13a2"
        },
        "node22": {
            "class": "TimeSeriesPlot",
            "module": "neuropype.nodes.visualization.TimeSeriesPlot",
            "params": {
                "absolute_time": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "antialiased": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "auto_line_colors": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "autoscale": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "decoration_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "downsampled": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "line_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#000000"
                },
                "line_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.75
                },
                "marker_color": {
                    "customized": false,
                    "type": "Port",
                    "value": "#FF0000"
                },
                "nans_as_zero": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "no_concatenate": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "override_srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "plot_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "plot_minmax": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "scale": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 10.0
                },
                "title": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "Time series view"
                },
                "zero_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#7F7F7F"
                },
                "zeromean": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                }
            },
            "uuid": "b6c8fa6e-fac1-4fd1-b1bc-e70661f8232b"
        },
        "node23": {
            "class": "LSLOutput",
            "module": "neuropype.nodes.network.LSLOutput",
            "params": {
                "chunk_len": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "ignore_signal_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "prediction_markers"
                },
                "marker_source_id": {
                    "customized": false,
                    "type": "StringPort",
                    "value": ""
                },
                "max_buffered": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 60
                },
                "reset_if_labels_changed": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "send_markers": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "source_id": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "(make sure to never use same string more than once on network)"
                },
                "srate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "stream_name": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Prediction"
                },
                "stream_type": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "Prediction"
                },
                "use_data_timestamps": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "use_numpy_optimization": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "df1560fa-d191-421b-aebf-e91ac9f39f75"
        },
        "node24": {
            "class": "OverrideAxis",
            "module": "neuropype.nodes.tensor_math.OverrideAxis",
            "params": {
                "axis_occurrence": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "carry_over_names": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "carry_over_numbers": {
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "custom_label": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "init_data": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "left",
                        "right"
                    ]
                },
                "new_axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "old_axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "only_signals": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "35e94774-6df4-4fa2-b504-66a97e816bb0"
        },
        "node25": {
            "class": "BarPlot",
            "module": "neuropype.nodes.visualization.BarPlot",
            "params": {
                "always_on_top": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "feature"
                },
                "background_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "#FFFFFF"
                },
                "bar_color": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "b"
                },
                "bar_width": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.33
                },
                "initial_dims": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        50,
                        50,
                        700,
                        500
                    ]
                },
                "instance_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "label_rotation": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "vertical"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "show_toolbar": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "title": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "LDA"
                },
                "use_last_instance": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "verbose": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "y_limits": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        0,
                        1
                    ]
                }
            },
            "uuid": "fee80da5-51bf-4772-ab41-26740462695f"
        },
        "node26": {
            "class": "LinearDiscriminantAnalysis",
            "module": "neuropype.nodes.machine_learning.LinearDiscriminantAnalysis",
            "params": {
                "class_weights": {
                    "customized": false,
                    "type": "Port",
                    "value": null
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "shrinkage": {
                    "customized": false,
                    "type": "Port",
                    "value": "auto"
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "eigen"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "7695ca49-679d-455a-ae33-9b4e22fa6982"
        },
        "node3": {
            "class": "CommonSpatialPatterns",
            "module": "neuropype.nodes.neural.CommonSpatialPatterns",
            "params": {
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "nof": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 3
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "c05727ba-bee7-4450-84d7-ce5ec8a139f9"
        },
        "node4": {
            "class": "Variance",
            "module": "neuropype.nodes.statistics.Variance",
            "params": {
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "time"
                },
                "degrees_of_freedom": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "force_feature_axis": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "5047f952-f40a-4d03-be13-5aaf5198f174"
        },
        "node5": {
            "class": "Logarithm",
            "module": "neuropype.nodes.elementwise_math.Logarithm",
            "params": {
                "base": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "53b815bc-c1db-45db-9d53-8702afe7e925"
        },
        "node6": {
            "class": "SelectRange",
            "module": "neuropype.nodes.tensor_math.SelectRange",
            "params": {
                "apply_multiple_axes": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": true,
                    "type": "EnumPort",
                    "value": "space"
                },
                "selection": {
                    "customized": true,
                    "type": "Port",
                    "value": "0:8"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "unit": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "indices"
                }
            },
            "uuid": "ee021b36-e07d-417d-abce-5992f31cc960"
        },
        "node7": {
            "class": "LogisticRegression",
            "module": "neuropype.nodes.machine_learning.LogisticRegression",
            "params": {
                "alphas": {
                    "customized": false,
                    "type": "ListPort",
                    "value": [
                        0.1,
                        0.5,
                        1.0,
                        5,
                        10.0
                    ]
                },
                "bias_scaling": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 1.0
                },
                "class_weights": {
                    "customized": true,
                    "type": "Port",
                    "value": "auto"
                },
                "cond_field": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "TargetValue"
                },
                "dont_reset_model": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "dual_formulation": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "include_bias": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "initialize_once": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "max_iter": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 100
                },
                "multiclass": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "ovr"
                },
                "num_folds": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 5
                },
                "num_jobs": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1
                },
                "probabilistic": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "regularizer": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "l2"
                },
                "search_metric": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "accuracy"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "solver": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "lbfgs"
                },
                "tolerance": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.0001
                },
                "verbosity": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                }
            },
            "uuid": "dbfa8ebe-c9fd-4ebf-92e9-d7fca1bfceb9"
        },
        "node8": {
            "class": "FIRFilter",
            "module": "neuropype.nodes.signal_processing.FIRFilter",
            "params": {
                "antisymmetric": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "axis": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "time"
                },
                "convolution_method": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "standard"
                },
                "cut_preringing": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "frequencies": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        6,
                        7,
                        30,
                        32
                    ]
                },
                "minimum_phase": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "mode": {
                    "customized": false,
                    "type": "EnumPort",
                    "value": "bandpass"
                },
                "order": {
                    "customized": false,
                    "type": "IntPort",
                    "value": null
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "stop_atten": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 50.0
                }
            },
            "uuid": "f7713a0c-01a4-4e38-ab7a-400282fcc968"
        },
        "node9": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": true,
                    "type": "ListPort",
                    "value": [
                        "Ch1",
                        "Ch2",
                        "Ch3",
                        "Ch4",
                        "Ch5",
                        "Ch6",
                        "Ch7",
                        "Ch8"
                    ]
                },
                "diagnostics": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                },
                "marker_query": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "type='Markers'"
                },
                "max_blocklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 1024
                },
                "max_buflen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 30
                },
                "max_chunklen": {
                    "customized": false,
                    "type": "IntPort",
                    "value": 0
                },
                "nominal_rate": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": null
                },
                "query": {
                    "customized": false,
                    "type": "StringPort",
                    "value": "type='EEG'"
                },
                "recover": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": true
                },
                "resolve_minimum_time": {
                    "customized": false,
                    "type": "FloatPort",
                    "value": 0.5
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "f5785705-eb96-44f7-8e79-8ca3cc6987d2"
        }
    },
    "version": 1.1
}</patch>
</scheme>
