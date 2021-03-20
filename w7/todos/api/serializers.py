from rest_framework import serializers
from api.models import TODOList, Task
from auth_.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        task = Task.objects.create(**validated_data)
        task.save()
        return task


class TODOListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TODOList
        fields = '__all__'


class TODOSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('get_tasks')

    class Meta:
        model = TODOList
        fields = ('id', 'name', 'tasks')

    def get_tasks(self, obj):
        completed = self.context.get("completed")
        tasks = Task.objects.filter(todo_list_id=obj.id)
        if completed:
            tasks = tasks.filter(completed=True)
        return TaskSerializer(tasks, many=True).data

