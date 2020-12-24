<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(72.0, 88.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="fd8a6503-ba20-48b1-8c2a-f75e73cd7078" version="1.0.0" />
		<node id="1" name="Time Series Plot" position="(756.0, 160.0)" project_name="NeuroPype" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" title="Time Series Plot" uuid="d6681703-c9c7-4bda-9c85-a9bc133dc975" version="1.0.1" />
		<node id="2" name="Record to XDF" position="(1050.0, 82.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="5a9aee78-db94-46a6-b00f-fd36d028213e" version="1.0.0" />
		<node id="3" name="Select Range" position="(632.0, 257.0)" project_name="NeuroPype" qualified_name="widgets.tensor_math.owselectrange.OWSelectRange" title="Select Range" uuid="62a860a7-fc08-4bfe-aa1b-5b35ec6781f9" version="1.0.0" />
		<node id="4" name="Rewrite Markers" position="(82.0, 246.0)" project_name="NeuroPype" qualified_name="widgets.markers.owrewritemarkers.OWRewriteMarkers" title="Rewrite Markers" uuid="e4d7a014-e633-49cf-affc-8c9fe201a90b" version="0.9.3" />
		<node id="5" name="Record to XDF" position="(1069.0, 453.0)" project_name="NeuroPype" qualified_name="widgets.file_system.owrecordtoxdf.OWRecordToXDF" title="Record to XDF" uuid="b53ee72a-5795-4c27-8ebd-5189bd6bdd3d" version="1.0.0" />
		<node id="6" name="Dejitter Timestamps" position="(220.0, 234.0)" project_name="NeuroPype" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" title="Dejitter Timestamps" uuid="e663075b-fbb3-43bf-a9f6-13a8c295171f" version="1.0.0" />
		<node id="7" name="FIR Filter" position="(741.0, 263.0)" project_name="NeuroPype" qualified_name="widgets.signal_processing.owfirfilter.OWFIRFilter" title="FIR Filter" uuid="6a883ec1-bafe-4c5f-abe4-fe32cbeaad5e" version="1.0.0" />
		<node id="8" name="Assign Target Values" position="(490.0, 260.0)" project_name="NeuroPype" qualified_name="widgets.machine_learning.owassigntargets.OWAssignTargets" title="Assign Targets" uuid="51fb9382-ed58-4095-85df-d71bd9e774b9" version="1.0.0" />
	</nodes>
	<links>
		<link enabled="true" id="0" sink_channel="Data" sink_node_id="2" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="1" sink_channel="Data" sink_node_id="1" source_channel="Data" source_node_id="0" />
		<link enabled="true" id="2" sink_channel="Data" sink_node_id="3" source_channel="Data" source_node_id="8" />
		<link enabled="true" id="3" sink_channel="Data" sink_node_id="7" source_channel="Data" source_node_id="3" />
		<link enabled="true" id="4" sink_channel="Data" sink_node_id="6" source_channel="Data" source_node_id="4" />
		<link enabled="true" id="5" sink_channel="Data" sink_node_id="5" source_channel="Data" source_node_id="7" />
		<link enabled="true" id="6" sink_channel="Data" sink_node_id="8" source_channel="Data" source_node_id="6" />
		<link enabled="true" id="7" sink_channel="Data" sink_node_id="4" source_channel="Data" source_node_id="0" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties format="pickle" node_id="0">gAN9cQAoWA0AAABjaGFubmVsX25hbWVzcQFdcQJYCwAAAGRpYWdub3N0aWNzcQOJWAwAAABtYXJr
ZXJfcXVlcnlxBFgOAAAAdHlwZT0nTWFya2VycydxBVgMAAAAbWF4X2Jsb2NrbGVucQZNAARYCgAA
AG1heF9idWZsZW5xB0seWAwAAABtYXhfY2h1bmtsZW5xCEsAWAwAAABub21pbmFsX3JhdGVxCVgN
AAAAKHVzZSBkZWZhdWx0KXEKWAUAAABxdWVyeXELWAoAAAB0eXBlPSdFRUcncQxYBwAAAHJlY292
ZXJxDYhYFAAAAHJlc29sdmVfbWluaW11bV90aW1lcQ5HP+AAAAAAAABYEwAAAHNhdmVkV2lkZ2V0
R2VvbWV0cnlxD2NzaXAKX3VucGlja2xlX3R5cGUKcRBYDAAAAFB5UXQ0LlF0Q29yZXERWAoAAABR
Qnl0ZUFycmF5cRJDLgHZ0MsAAQAAAAADBAAAAZcAAAR7AAACYgAAAwwAAAG2AAAEcwAAAloAAAAA
AABxE4VxFIdxFVJxFlgOAAAAc2V0X2JyZWFrcG9pbnRxF4l1Lg==
</properties>
		<properties format="pickle" node_id="1">gAN9cQAoWA0AAABhYnNvbHV0ZV90aW1lcQGJWA0AAABhbHdheXNfb25fdG9wcQKJWAsAAABhbnRp
YWxpYXNlZHEDiFgQAAAAYXV0b19saW5lX2NvbG9yc3EEiVgJAAAAYXV0b3NjYWxlcQWIWBAAAABi
YWNrZ3JvdW5kX2NvbG9ycQZYBwAAACNGRkZGRkZxB1gQAAAAZGVjb3JhdGlvbl9jb2xvcnEIWAcA
AAAjMDAwMDAwcQlYCwAAAGRvd25zYW1wbGVkcQqJWAwAAABpbml0aWFsX2RpbXNxC11xDChLMksy
TbwCTfQBZVgKAAAAbGluZV9jb2xvcnENWAcAAAAjMDAwMDAwcQ5YCgAAAGxpbmVfd2lkdGhxD0c/
6AAAAAAAAFgMAAAAbWFya2VyX2NvbG9ycRBYBwAAACNGRjAwMDBxEVgMAAAAbmFuc19hc196ZXJv
cRKJWA4AAABub19jb25jYXRlbmF0ZXETiVgOAAAAb3ZlcnJpZGVfc3JhdGVxFFgNAAAAKHVzZSBk
ZWZhdWx0KXEVWAwAAABwbG90X21hcmtlcnNxFohYCwAAAHBsb3RfbWlubWF4cReIWBMAAABzYXZl
ZFdpZGdldEdlb21ldHJ5cRhjc2lwCl91bnBpY2tsZV90eXBlCnEZWAwAAABQeVF0NC5RdENvcmVx
GlgKAAAAUUJ5dGVBcnJheXEbQy4B2dDLAAEAAAAAAwQAAAE1AAAEewAAAsMAAAMMAAABVAAABHMA
AAK7AAAAAAAAcRyFcR2HcR5ScR9YBQAAAHNjYWxlcSBHP/AAAAAAAABYDgAAAHNldF9icmVha3Bv
aW50cSGJWAwAAABzaG93X3Rvb2xiYXJxIohYCwAAAHN0cmVhbV9uYW1lcSNYDQAAACh1c2UgZGVm
YXVsdClxJFgKAAAAdGltZV9yYW5nZXElSwhYBQAAAHRpdGxlcSZYEAAAAFRpbWUgc2VyaWVzIHZp
ZXdxJ1gKAAAAemVyb19jb2xvcnEoWAcAAAAjN0Y3RjdGcSlYCAAAAHplcm9tZWFucSqIdS4=
</properties>
		<properties format="pickle" node_id="2">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYFgAAAGNvbnRyb2wtMi10cmFpbmluZy54ZGZxDVgLAAAAb3V0cHV0X3Jvb3RxDlgQAAAA
RTovYmNpL2RhdGEveGRmL3EPWAsAAAByZXRyaWV2YWJsZXEQiVgTAAAAc2F2ZWRXaWRnZXRHZW9t
ZXRyeXERY3NpcApfdW5waWNrbGVfdHlwZQpxElgMAAAAUHlRdDQuUXRDb3JlcRNYCgAAAFFCeXRl
QXJyYXlxFEMuAdnQywABAAAAAAMEAAABRAAABHsAAAK0AAADDAAAAWMAAARzAAACrAAAAAAAAHEV
hXEWh3EXUnEYWA0AAABzZXNzaW9uX25vdGVzcRloBVgOAAAAc2V0X2JyZWFrcG9pbnRxGolYBwAA
AHZlcmJvc2VxG4l1Lg==
</properties>
		<properties format="literal" node_id="3">{'apply_multiple_axes': False, 'axis': 'space', 'savedWidgetGeometry': None, 'selection': '0:8', 'set_breakpoint': False, 'unit': 'indices'}</properties>
		<properties format="literal" node_id="4">{'iv_column': 'Marker', 'pattern_syntax': 'wildcards', 'regex_sub': False, 'remove_all_others': True, 'rules': "{'3': '0', '4': '1'}", 'savedWidgetGeometry': None, 'set_breakpoint': False}</properties>
		<properties format="pickle" node_id="5">gAN9cQAoWAwAAABhbGxvd19kb3VibGVxAYlYDwAAAGNsb3NlX29uX21hcmtlcnECWA8AAABjbG9z
ZS1yZWNvcmRpbmdxA1gNAAAAY2xvdWRfYWNjb3VudHEEWAAAAABxBVgMAAAAY2xvdWRfYnVja2V0
cQZoBVgRAAAAY2xvdWRfY3JlZGVudGlhbHNxB2gFWAoAAABjbG91ZF9ob3N0cQhYBwAAAERlZmF1
bHRxCVgOAAAAY2xvdWRfcGFydHNpemVxCkseWAwAAABkZWxldGVfcGFydHNxC4hYCAAAAGZpbGVu
YW1lcQxYKgAAAEU6L2JjaS9kYXRhL3hkZi9mdGQtY29udHJvbC0yLXRyYWluaW5nLnhkZnENWAsA
AABvdXRwdXRfcm9vdHEOaAVYCwAAAHJldHJpZXZhYmxlcQ+JWBMAAABzYXZlZFdpZGdldEdlb21l
dHJ5cRBjc2lwCl91bnBpY2tsZV90eXBlCnERWAwAAABQeVF0NC5RdENvcmVxElgKAAAAUUJ5dGVB
cnJheXETQy4B2dDLAAEAAAAAAwQAAAFEAAAEewAAArQAAAMMAAABYwAABHMAAAKsAAAAAAAAcRSF
cRWHcRZScRdYDQAAAHNlc3Npb25fbm90ZXNxGGgFWA4AAABzZXRfYnJlYWtwb2ludHEZiVgHAAAA
dmVyYm9zZXEaiXUu
</properties>
		<properties format="literal" node_id="6">{'force_monotonic': True, 'forget_halftime': 300, 'max_updaterate': 500, 'savedWidgetGeometry': None, 'set_breakpoint': False, 'warmup_samples': -1}</properties>
		<properties format="literal" node_id="7">{'antisymmetric': False, 'axis': 'time', 'convolution_method': 'standard', 'cut_preringing': False, 'frequencies': [6, 7, 30, 32], 'minimum_phase': True, 'mode': 'bandpass', 'order': '(use default)', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'stop_atten': 50.0}</properties>
		<properties format="literal" node_id="8">{'also_legacy_output': False, 'is_categorical': False, 'iv_column': 'Marker', 'mapping': {'0': 0, '1': 1}, 'mapping_format': 'compat', 'savedWidgetGeometry': None, 'set_breakpoint': False, 'support_wildcards': False, 'use_numbers': False, 'verbose': False}</properties>
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
            "node1",
            "data",
            "node3",
            "data"
        ],
        [
            "node1",
            "data",
            "node2",
            "data"
        ],
        [
            "node1",
            "data",
            "node5",
            "data"
        ],
        [
            "node9",
            "data",
            "node4",
            "data"
        ],
        [
            "node4",
            "data",
            "node8",
            "data"
        ],
        [
            "node5",
            "data",
            "node7",
            "data"
        ],
        [
            "node8",
            "data",
            "node6",
            "data"
        ],
        [
            "node7",
            "data",
            "node9",
            "data"
        ]
    ],
    "nodes": {
        "node1": {
            "class": "LSLInput",
            "module": "neuropype.nodes.network.LSLInput",
            "params": {
                "channel_names": {
                    "customized": false,
                    "type": "ListPort",
                    "value": []
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
            "uuid": "fd8a6503-ba20-48b1-8c2a-f75e73cd7078"
        },
        "node2": {
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
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
                    "customized": true,
                    "type": "BoolPort",
                    "value": true
                },
                "stream_name": {
                    "customized": false,
                    "type": "StringPort",
                    "value": null
                },
                "time_range": {
                    "customized": true,
                    "type": "FloatPort",
                    "value": 8
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
            "uuid": "d6681703-c9c7-4bda-9c85-a9bc133dc975"
        },
        "node3": {
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
                    "value": "control-2-training.xdf"
                },
                "output_root": {
                    "customized": true,
                    "type": "StringPort",
                    "value": "E:/bci/data/xdf/"
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
            "uuid": "5a9aee78-db94-46a6-b00f-fd36d028213e"
        },
        "node4": {
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
            "uuid": "62a860a7-fc08-4bfe-aa1b-5b35ec6781f9"
        },
        "node5": {
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
                    "value": "{'3': '0', '4': '1'}"
                },
                "set_breakpoint": {
                    "customized": false,
                    "type": "BoolPort",
                    "value": false
                }
            },
            "uuid": "e4d7a014-e633-49cf-affc-8c9fe201a90b"
        },
        "node6": {
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
                    "value": "E:/bci/data/xdf/ftd-control-2-training.xdf"
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
            "uuid": "b53ee72a-5795-4c27-8ebd-5189bd6bdd3d"
        },
        "node7": {
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
            "uuid": "e663075b-fbb3-43bf-a9f6-13a8c295171f"
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
            "uuid": "6a883ec1-bafe-4c5f-abe4-fe32cbeaad5e"
        },
        "node9": {
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
                        "0": 0,
                        "1": 1
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
            "uuid": "51fb9382-ed58-4095-85df-d71bd9e774b9"
        }
    },
    "version": 1.1
}</patch>
</scheme>