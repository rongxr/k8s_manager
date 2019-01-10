# -*- coding: utf-8 -*-
from .models import Assets, Product, ProductVersion, KubeConfig, Server
from django.forms import ModelForm
from django.forms import widgets as wid
from . import common

class AssetsForm(ModelForm):
    class Meta:
        model = Assets
        fields = ('assets_type','status','idc','cabinet_no','cabinet_order','tags','id')
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
        # error_messages = {
        #     'name':{'required':"用户名不能为空",},
        #     'age':{'required':"年龄不能为空",},
        # }
        widgets = {
            "assets_type": wid.Select(choices=common.TYPE_VALUE),
            "status": wid.Select(choices=common.STATUS_VALUE),
            "idc": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：10.24.22.12"}),
            "cabinet_no": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：10.24.22.12"}),
            "cabinet_order": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：10.24.22.12"}),
            "tags": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：阿里云 高配"}),
            "id": wid.HiddenInput()
        }
        labels= {
            "idc": "IDC机房(可选)",
            "cabinet_no": "机柜号(可选)",
            "cabinet_order": "机柜中序号(可选)",
            "tags": "资产标签(可选)" 
        }

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','product_wiki','product_manager','product_contact','dev_manager','dev_contact','qa_manager','qa_contact','safe_manager','safe_contact',
            'product_desc','id'
        )
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
        widgets = {
            "product_name": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：支付系统"}),
            "product_wiki": wid.TextInput(attrs={'class':'smallinput'}),
            "product_manager": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：张启山"}),
            "product_contact": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：qishan.zhang@gmail.com"}),
            "dev_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "dev_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "qa_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "qa_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "safe_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "safe_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "product_desc": wid.Textarea(attrs={'cols': 80, 'rows': 5, 'class':'mediuminput'}),
            "id": wid.HiddenInput()
        }

class ProductVersionForm(ModelForm):
    class Meta:
        model = ProductVersion
        fields = ('version_name','tags','version_status','start_time','end_time','version_wiki','product_manager','product_contact',
            'dev_manager','dev_contact','qa_manager','qa_contact','safe_manager','safe_contact','id')
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
        widgets = {
            "version_name": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：v2.1.0"}),
            "tags": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：uat,payment,v2.0.0或者uat|payment|v2.0.0"}),
            "version_status": wid.Select(choices=common.VERSION_STATUS_VALUE),
            "start_time": wid.TextInput(attrs={'class':'smallinput'}),
            "end_time": wid.TextInput(attrs={'class':'smallinput'}),
            "version_wiki": wid.TextInput(attrs={'class':'smallinput'}),
            "product_manager": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：张启山"}),
            "product_contact": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：qishan.zhang@gmail.com"}),
            "dev_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "dev_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "qa_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "qa_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "safe_manager": wid.TextInput(attrs={'class':'smallinput'}),
            "safe_contact": wid.TextInput(attrs={'class':'smallinput'}),
            "id": wid.HiddenInput()
        }

class KubeConfigForm(ModelForm):
    class Meta:
        model = KubeConfig
        fields = ('kube_name','kube_version','deploy_mode','ntp_enabled','lb_node','etcd_node','etcd_node_name_prefix','kube_master','kube_node','harbor_node',
                    'harbor_domain','harbor_install',
                    #'kube_new_master','kube_new_node',
                    'ssh_addkey','node_port_range','master_ip','kube_api_server','cluster_network',
                    'service_cidr',
                    'cluster_cidr','cluster_k8s_svc_ip','cluster_dns_svc_ip','cluster_dns_domain',
                    'basic_auth_user','basic_auth_pass','bin_dir','ca_dir','base_dir','kube_desc',
                    'id','deploy'
        )
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
        widgets = {
            "kube_name": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：Test"}),
            "kube_version": wid.Select(choices=common.K8S_VERSION),
            "deploy_mode": wid.Select(choices=common.K8S_DEPLOY_MODE),
            "ntp_enabled": wid.Select(choices=common.COMMON_STATUS),

            "lb_node": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.185;192.168.150.187"}),
            "etcd_node": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.181;192.168.150.182;192.168.150.183"}),
            "etcd_node_name_prefix": wid.TextInput(attrs={'class':'smallinput', 'value': 'etcd'}),
            "kube_master": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.181;192.168.150.182"}),
            "kube_node": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.184"}),

            "harbor_node": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.189"}),
            "harbor_domain": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：harbor.ikang.com"}),
            "harbor_install": wid.Select(choices=common.COMMON_STATUS),

            #"kube_new_master": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.181;192.168.150.182"}),
            #"kube_new_node": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.184"}),
            "ssh_addkey": wid.Select(choices=common.COMMON_STATUS),
            "node_port_range": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：20000-40000"}),

            "master_ip": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.150.187"}),
            "kube_api_server": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：https://$master_ip:8443"}),

            "cluster_network": wid.Select(choices=common.K8S_CLUSTER_NETWORK),

            "service_cidr": wid.TextInput(attrs={'class':'smallinput', 'value':"10.68.0.0/16"}),
            "cluster_cidr": wid.TextInput(attrs={'class':'smallinput', 'value':"172.20.0.0/16"}),
            "cluster_k8s_svc_ip": wid.TextInput(attrs={'class':'smallinput', 'value':"10.68.0.1"}),
            "cluster_dns_svc_ip": wid.TextInput(attrs={'class':'smallinput', 'value':"10.68.0.2"}),
            "cluster_dns_domain": wid.TextInput(attrs={'class':'smallinput', 'value':"cluster.local."}),

            "basic_auth_user": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：admin"}),
            "basic_auth_pass": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：admin123456"}),

            "bin_dir": wid.TextInput(attrs={'class':'smallinput', 'readonly': 'readonly','value': '/opt/kube/bin'}),
            "ca_dir": wid.TextInput(attrs={'class':'smallinput', 'readonly': 'readonly','value': '/etc/kubernetes/ssl'}),
            "base_dir": wid.TextInput(attrs={'class':'smallinput', 'readonly': 'readonly','value': '/etc/ansible'}),
            
            "kube_desc": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"集群描述信息"}),
            "id": wid.HiddenInput(),
            "deploy": wid.HiddenInput(),
        }

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ('manage_ip','intranet_ip','user','ip','port','desc','sn','manufacturer',
            'model','platform','version','cpu_count','cpu_physical_count','cpu_model','mac',
            'serial_num','name','port_num','id')
        exclude = None          #排除的字段
        labels = None           #提示信息
        help_texts = None       #帮助提示信息
        widgets = None          #自定义插件
        error_messages = None   #自定义错误信息
        widgets = {
            "manage_ip": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：10.24.22.12"}),
            "intranet_ip": wid.TextInput(attrs={'class':'smallinput', 'placeholder':"如：192.168.1.240"}),
            "user": wid.Select(choices=common.VERSION_STATUS_VALUE),
            "ip": wid.TextInput(attrs={'class':'smallinput','placeholder': "如：23.24.22.12"}),
            "port": wid.TextInput(attrs={'class':'smallinput'}),
            "desc": wid.Textarea(attrs={'class':'smallinput','placeholder': "如：本地机房服务器，在2楼xxx办公室"}),

            "sn": wid.TextInput(attrs={'class':'smallinput', 'readonly': "readonly"}),
            "manufacturer": wid.TextInput(attrs={'class':'smallinput', 'readonly': "readonly"}),
            "model": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "platform": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "version": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "cpu_count": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "cpu_physical_count": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "cpu_model": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "mac": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "serial_num": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "name": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "port_num": wid.TextInput(attrs={'class':'smallinput','readonly': "readonly"}),
            "id": wid.HiddenInput(),
        }






