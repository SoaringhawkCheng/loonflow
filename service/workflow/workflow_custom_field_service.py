import json
from apps.workflow.models import CustomField
from service.base_service import BaseService
from service.common.log_service import auto_log


class WorkflowCustomFieldService(BaseService):
    def __init__(self):
        pass

    @classmethod
    @auto_log
    def get_workflow_custom_field(cls, workflow_id):
        """
        获取工作流的自定义字段信息
        :param workflow_id:
        :return:
        """
        custom_field_queryset = CustomField.objects.filter(workflow_id=workflow_id, is_deleted=0).all()
        format_custom_field_dict = {}
        for custom_field in custom_field_queryset:
            if custom_field.label:
                label = custom_field.label
            else:
                label = '{}'
            format_custom_field_dict[custom_field.field_key] = dict(workflow_id=custom_field.workflow_id, field_type_id=custom_field.field_type_id,
                                                                    field_name=custom_field.field_name,order_id=custom_field.order_id,
                                                                    default_value=custom_field.default_value, description=custom_field.description,
                                                                    field_template=custom_field.field_template, boolean_field_display=custom_field.boolean_field_display,
                                                                    field_choice=custom_field.field_choice, label=label)
        return format_custom_field_dict, ''

    @classmethod
    @auto_log
    def get_workflow_custom_field_name_list(cls, workflow_id):
        """
        获取工作流自定义字段list
        :param workflow_id:
        :return:
        """
        custom_field_queryset = CustomField.objects.filter(workflow_id=workflow_id, is_deleted=0).all()
        return [custom_field.field_key for custom_field in custom_field_queryset], ''
