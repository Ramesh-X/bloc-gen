import 'dart:async';

import 'package:bloc/bloc.dart';
import 'package:fcode_common/fcode_common.dart';
import 'package:flutter/material.dart';

import 'template_event.dart';
import 'template_state.dart';

class TemplateBloc extends Bloc<TemplateEvent, TemplateState> {
  static final log = Log("TemplateBloc");

  TemplateBloc(BuildContext context);

  @override
  TemplateState get initialState => TemplateState(
        error: '',
      );

  @override
  Stream<TemplateState> mapEventToState(TemplateEvent event) async* {
    switch (event.runtimeType) {
      case ErrorEvent:
        final error = (event as ErrorEvent).error;
        log.e('Error: $error');
        yield state.clone(error: "");
        yield state.clone(error: error);
        break;
    }
  }

  @override
  void onError(Object error, StackTrace stacktrace) {
    log.e('$error');
    log.e('$stacktrace');
    _addErr(error);
  }

  @override
  Future<void> close() async {
    await super.close();
  }

  void _addErr(e) {
    try {
      add(ErrorEvent(
        (e is String) ? e : (e.message ?? "Something went wrong. Please try again !"),
      ));
    } catch (e) {
      add(ErrorEvent("Something went wrong. Please try again !"));
    }
  }
}
