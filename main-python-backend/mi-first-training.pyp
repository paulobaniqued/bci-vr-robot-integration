<?xml version='1.0' encoding='utf-8'?>
<scheme description="" title="" version="2.0">
	<nodes>
		<node id="0" name="LSL Input" position="(211.0, 228.0)" project_name="NeuroPype" qualified_name="widgets.network.owlslinput.OWLSLInput" title="LSL Input" uuid="5e4dd8a4-7f19-4383-8dbe-66bae1ff776e" version="1.0.0" />
	</nodes>
	<links />
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
    "edges": [],
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
            "uuid": "5e4dd8a4-7f19-4383-8dbe-66bae1ff776e"
        }
    },
    "version": 1.1
}</patch>
</scheme>
