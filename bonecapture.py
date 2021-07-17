import hou 

subnet = hou.node('/obj/rigg_test').createNode('subnet', 'bonecapture')
subnet.createNode('bonecapturelines')
subnet.createNode('tetconform')
subnet.createNode('bonecapturebiharmonic')
subnet.createNode('timeshift')
subnet.createNode('capturelayerpaint')

subnet.layoutChildren()
