from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			# the method is a safe method
			return True
		else:
			"""
				not a safe method and only owners are granted permissions
				for unsafe methods
			"""
			return obj.user == request.user


# Needs modification

class IsStaffOrReadOnly(permissions.BasePermission):
	
	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:

			return request.user.is_staff
